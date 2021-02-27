# _*_ coding:utf-8 _*_ 

'''
创建时间：2020-10-09
文件说明：Pyqt5 开发的客户端，调用打印机
'''

# _*_ coding:utf-8 _*_ 
# Python3.6.8 + Pyqt5
# ——创建时间：2020.7.16——
# 登录页面

import sys
import os
import time
import json
import requests
import webbrowser
import configparser
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineScript, QWebEnginePage
from PyQt5 import QtMultimedia
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
from app.kill_port import killPort
from threading import Thread

# conf = configparser.ConfigParser()
# conf.read(BASE_DIR + '/config/config.ini')  # 文件路径
# tim = int(conf.get('tim', 'stime'))


def read(state):
	filepath = "./config/token.txt"
	if state == "r":
		with open(filepath, 'r', encoding='utf-8') as f:
			data = f.read()
			f.close()
		return data
	else:
		with open(filepath, 'w', encoding='utf-8') as f:
			f.write(str(-1))
			f.close()
		return "ok"

# 异步调用函数装饰器
def async(func):
	def wrapper(*args, **kwargs):
		thr = Thread(target=func, args=args, kwargs=kwargs)
		thr.start()
	return wrapper

# 创建播放声音的线程类
class PlayFile(QThread):
	# progressBarValue = pyqtSignal(int)  # 更新进度条

	def __init__(self):
		super(PlayFile, self).__init__()

	def run(self):
		while True:
			time.sleep(10)
			# 请求php的接口，返回是否有新订单
			uniacid = read("r")
			data = {"uniacid":uniacid}
			response = requests.post(url="http://application.wupin.shop/api/getOrderNum",data=data)
			result = json.loads(response.text)
			if result.get("data") > 0:
				# 打开订单页
				webbrowser.open_new_tab('http://business.wupin.shop/index.html#/orderList')
				# 播放音频
				filepath = './static/mp3/ttsdemo_1609153544.mp3'          # 音频文件路径
				yfile = QUrl.fromLocalFile(filepath)
				content = QtMultimedia.QMediaContent(yfile)
				player = QtMultimedia.QMediaPlayer()
				player.setMedia(content)
				player.setVolume(50.0)
				player.play()
			time.sleep(300)
		# self.progressBarValue.emit(1)  # 发送进度条的值信号

class TrayIcon(QSystemTrayIcon):
	def __init__(self, parent=None):
		super(TrayIcon, self).__init__(parent)
		self.showMenu()
		self.other()

	def showMenu(self):
		"设计托盘的菜单，这里我实现了一个二级菜单"
		self.menu = QMenu()
		self.showAction1 = QAction(QIcon("./static/image/index.ico"),"打开后台", self, triggered=self.mClied)
		self.showAction2 = QAction(QIcon("./static/image/info.ico"),"关于我们", self,triggered=self.showM)
		self.quitAction = QAction(QIcon("./static/image/quit.ico"),"退出", self, triggered=self.quit)

		self.menu.addAction(self.showAction1)
		self.menu.addAction(self.showAction2)
		self.menu.addAction(self.quitAction)
		# self.menu1.setTitle("二级菜单")
		self.setContextMenu(self.menu)

	def other(self):
		self.activated.connect(self.iconClied)
		#把鼠标点击图标的信号和槽连接
		self.messageClicked.connect(self.mClied)
		#把鼠标点击弹出消息的信号和槽连接
		self.setIcon(QIcon("./static/image/favicon.ico"))
		self.icon = self.MessageIcon()
		#设置图标

	def iconClied(self, reason):
		"鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
		if reason == 2 or reason == 3:
			pw = self.parent()
			if pw.isVisible():
				pw.hide()

	def mClied(self):
		# self.showMessage("程序介绍", "是一款连接打印机打印程序，希望给您带来更好的体验。", self.icon)
		webbrowser.open_new_tab('http://business.wupin.shop/index.html')

	def showM(self):
		self.showMessage("关于我们", "中国诚信商品数据库\n联系电话：028-68486409")

	def quit(self):
		"保险起见，为了完整的退出"
		# 修改token值
		read("w")
		killPort(8088)
		self.setVisible(False)
		qApp.quit()
		sys.exit()


# 所有的页面
class LoginDialog(QDialog, QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# 语音播放线程
		self.thread_1 = PlayFile()
		self.thread_1.start()
		# 显示托盘
		ti = TrayIcon(self)
		ti.show()
		# 启动企业客户端
		webbrowser.open_new_tab('http://business.wupin.shop/index.html')

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = LoginDialog()
	# window.show()
	# channel = QWebChannel()
	try:
		@async
		def run():
			try:
				from app import app
				app.runserver()
			except Exception as e:
				print(e)
				print('8088端口被占用')
		run()
	except:
		print("端口被占用")
	sys.exit(app.exec())
