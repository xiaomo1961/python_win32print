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
import uuid
import hashlib
import requests
import ast
import json
import socket
import requests
import configparser
import webbrowser
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QSystemTrayIcon, QDialog, QMainWindow, QApplication, QMenu, QAction, qApp
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QTimer, pyqtSignal, QThread, QUrl
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineScript, QWebEnginePage
from PyQt5 import QtMultimedia
Base_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_DIR)

from threading import Thread
from client.UiNotify import Ui_NotifyForm

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
            # 请求php的接口，返回是否有新订单
            response = requests.post(url="http://192.168.1.131:8088/play")
            result = json.loads(response.text)
            print(result)
            if result.get("num") > 0:
                # 播放音频
                filepath = Base_DIR + '/static/mp3/ttsdemo_1609153544.mp3'          # 音频文件路径
                yfile = QUrl.fromLocalFile(filepath)
                content = QtMultimedia.QMediaContent(yfile)
                player = QtMultimedia.QMediaPlayer()
                player.setMedia(content)
                player.setVolume(50.0)
                player.play()
                time.sleep(10)
        # self.progressBarValue.emit(1)  # 发送进度条的值信号

class TrayIcon(QSystemTrayIcon, QWidget, Ui_NotifyForm):
    def __init__(self, title="", content="", timeout=5000, *args, **kwargs):
        super(TrayIcon, self).__init__(*args, **kwargs)
        print(0)
        # try:
        #     self.setupUi(self)
        # except Exception as e:
        #     print(e)
        print(1)
        self.showMenu()
        self.other()
        # self._init()

    def showMenu(self):
        "设计托盘的菜单，这里我实现了一个二级菜单"
        self.menu = QMenu()
        self.showAction1 = QAction("打开后台", self, triggered=self.mClied)
        self.showAction2 = QAction("关于我们", self,triggered=self.showM)
        self.quitAction = QAction("退出", self, triggered=self.quit)

        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        # self.menu1.setTitle("二级菜单")
        self.setContextMenu(self.menu)

    def onClose(self):
        #点击关闭按钮时
        print("onClose")
        self.isShow = False
        QTimer.singleShot(100, self.closeAnimation)#启动弹回动画

    # 弹框设置
    def _init(self):
        # 隐藏任务栏|去掉边框|顶层显示
        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # 关闭按钮事件
        self.buttonClose.clicked.connect(self.onClose)
        # 点击查看按钮
        self.buttonView.clicked.connect(self.onView)
        # 是否在显示标志
        self.isShow = True
        # 超时
        self._timeouted = False
        # 桌面
        self._desktop = QApplication.instance().desktop()
        # 窗口初始开始位置
        self._startPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.screenGeometry().height()
        )
        # 窗口弹出结束位置
        self._endPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.availableGeometry().height() - self.height() - 5
        )
        # 初始化位置到右下角
        self.move(self._startPos)

        # 动画
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.finished.connect(self.onAnimationEnd)
        self.animation.setDuration(1000)  # 1s

        # 弹回定时器
        self._timer = QTimer(self, timeout=self.closeAnimation)
    
    def show1(self, title="", content="", timeout=5000):
        self._timer.stop()  # 停止定时器,防止第二个弹出窗弹出时之前的定时器出问题
        self.hide()  # 先隐藏
        self.move(self._startPos)  # 初始化位置到右下角
        super(WindowNotify, self).show1()
        self.setTitle(title).setContent("您有新订单啦").setTimeout(timeout)
        return self

    def showAnimation(self):
        print("showAnimation isShow = True")
        # 显示动画
        self.isShow = True
        self.animation.stop()#先停止之前的动画,重新开始
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._endPos)
        self.animation.start()
        # 弹出5秒后,如果没有焦点则弹回去
        self._timer.start(self._timeout)
#         QTimer.singleShot(self._timeout, self.closeAnimation)

    def closeAnimation(self):
        print("closeAnimation hasFocus", self.hasFocus())
        # 关闭动画
        if self.hasFocus():
            # 如果弹出后倒计时5秒后还有焦点存在则失去焦点后需要主动触发关闭
            self._timeouted = True
            return  # 如果有焦点则不关闭
        self.isShow = False
        self.animation.stop()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._startPos)
        self.animation.start()

    def onAnimationEnd(self):
        # 动画结束
        print("onAnimationEnd isShow", self.isShow)
        if not self.isShow:
            print("onAnimationEnd close()")
            self.close()
            print("onAnimationEnd stop timer")
            self._timer.stop()
            print("onAnimationEnd close and emit signal")
            self.SignalClosed.emit()
    
    def enterEvent(self, event):
        super(WindowNotify, self).enterEvent(event)
        # 设置焦点(好像没啥用,不过鼠标点击一下后,该方法就有用了)
        print("enterEvent setFocus Qt.MouseFocusReason")
        self.setFocus(Qt.MouseFocusReason)

    def leaveEvent(self, event):
        super(WindowNotify, self).leaveEvent(event)
        # 取消焦点
        print("leaveEvent clearFocus")
        self.clearFocus()
        if self._timeouted:
            QTimer.singleShot(1000, self.closeAnimation)

    def other(self):
        self.activated.connect(self.iconClied)
        #把鼠标点击图标的信号和槽连接
        self.messageClicked.connect(self.mClied)
        #把鼠标点击弹出消息的信号和槽连接
        self.setIcon(QIcon("../static/image/favicon.ico"))
        self.icon = self.MessageIcon()
        #设置图标

    def iconClied(self, reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2 or reason == 3:
            pw = self.parent()
            # print(pw)
            if pw.isVisible():
                pw.hide()

    def mClied(self):
        # self.showMessage("程序介绍", "是一款连接打印机打印程序，希望给您带来更好的体验。", self.icon)
        webbrowser.open_new_tab('http://business.wupin.shop/index.html')

    def showM(self):
        self.showMessage("关于我们", "四川中新华搜技术有限公司\n联系电话：123456", self.icon)

    def quit(self):
        "保险起见，为了完整的退出"
        self.setVisible(False)
        # self.parent().exit()
        qApp.quit()
        sys.exit()


# 所有的页面
class LoginDialog(QDialog, QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 语音播放线程
        self.thread_1 = PlayFile()
        # self.thread_1.progressBarValue.connect(1)
        self.thread_1.start()
        # 显示托盘
        ti = TrayIcon(self)
        ti.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginDialog()
    # window.show()
    # channel = QWebChannel()
    

    # try:
    #     @async
    #     def run():
    #         try:
    #             from app import app
    #             app.runserver()
    #         except Exception as e:
    #             print(e)
    #             print('8088端口被占用')
    #     run()
    # except:
    #     print("端口被占用")
    sys.exit(app.exec())
