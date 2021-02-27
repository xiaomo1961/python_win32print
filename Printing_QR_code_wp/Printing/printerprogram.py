# _*_ coding:utf-8 _*_

'''
创建时间：2020-10-14
文件说明：调用打印机程序，打印标签
'''
import os
import sys
import win32print
import win32ui
import win32con
import json
import configparser
from PIL import Image, ImageWin
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Printing import AlignText
from Generate_QR_code import generate_QR

conf = configparser.ConfigParser()
conf.read(BASE_DIR + '/config/config.ini')  # 文件路径
Orientation = conf.get('printer', 'Orientation')
TextAligndict = AlignText.TextAlign
# 创建一个打印机类
class Printer(object):
	'''
	创建打印机程序，连接打印机
	设置打印机，
	加载打印模版，
	打印标签
	'''

	def __init__(self):
		# 获取打印机驱动名称(系统默认的打印机)
		self.printer_name = win32print.GetDefaultPrinter()
		# 打开打印机默认阈值
		self.Defaults  = {"DesiredAccess":win32print.PRINTER_ALL_ACCESS}
		# 打印机对象
		self.pHandle = None
		# 
		self.hDC = None
		

	# 连接打开打印机
	def open_printer(self, printername):
		'''
		打开打印机的两种方法
		1，用户指定驱动连接打印机
		2，获取系统默认驱动连接打印机
		'''
		if not printername:
			# 驱动名称为空，获取系统默认驱动连接打印机
			self.pHandle = win32print.OpenPrinter(self.printer_name, self.Defaults)

		else:
			# 模版设置了驱动名称，使用设置的驱动名称连接打印机
			self.pHandle = win32print.OpenPrinter(printername, self.Defaults)


	# 设置打印机的纸张
	def setting_printer(self, setting):
		'''
		设置打印机纸张大小
		PaperWidth 纸张宽度
		PaperLength 纸张高度
		'''
		# 获取打印机的配置参数
		try:
			attributes = win32print.GetPrinter(self.pHandle, 2)
			attributes.get("pDevMode").PaperWidth = setting.get("PaperWidth") * 10
			attributes.get("pDevMode").PaperLength = setting.get("PaperLength") * 10
			# 设置打印方向 Orientation=1 表示纵向打印，Orientation=2 表示横向打印
			attributes.get("pDevMode").Orientation = int(setting.get("Orientation"))
			win32print.SetPrinter(self.pHandle, 2, attributes, 0)
		except Exception as e:
			print(e)
			print("打印机配置失败")

	# 创建pyCDC对象
	def establish_pyCDC(self, filename, setting, PrinterName):
		'''
		创建打印对象
		'''
		try:
			self.hDC = win32ui.CreateDC()
			self.hDC.CreatePrinterDC(PrinterName)
			# 开始将文档假脱机保存到打印机CDC
			self.hDC.StartDoc(filename)
			# 在打印机DC上启动一个新页面
			self.hDC.StartPage()
			# 设置设备上下文的映射模式
			# 映射模式 MM_ANISOTROPIC, MM_HIENGLISH, MM_HIMETRIC, MM_ISOTROPIC, MM_LOENGLISH, MM_LOMETRIC, MM_TEXT, MM_TWIPS
			self.hDC.SetMapMode(win32con.MM_ISOTROPIC)
			# 设置纸张大小
			self.hDC.SetWindowExt((setting.get("PaperWidth"), setting.get("PaperLength")))
		except Exception as e:
			print("创建CDC对象失败")

	# 打印二维码设置
	def print_image(self, image):
		'''
		打开图片，缩放并打印出来
		'''
		# 首先生成二维码
		save_path = BASE_DIR  + "/static/code/"
		generate_QR.create_code(image.get("url"), "code", save_path)
		bmp = Image.open(save_path + "code.png")
		if bmp.size[0] < bmp.size[1]:
			bmp = bmp.rotate(90)
		scale = 1

		dib = ImageWin.Dib(bmp)
		scaled_width, scaled_height = [int(scale * i) for i in bmp.size]
		dib.draw(self.hDC.GetHandleOutput(), (image.get("x1"), image.get("y1"), image.get("x2"), image.get("y2")))

	# 打印文字
	def print_words(self, words):
		for w in words:
			win32font = win32ui.CreateFont(w.get("font"))
			# 设置字体属性
			self.hDC.SelectObject(win32font)
			# 设置文本对齐
			if w.get("textalogn") != None:
				self.hDC.SetTextAlign(TextAligndict.get(w.get("textalogn")))
			self.hDC.TextOut(w.get("x"), w.get("y"), w.get("text"))

	# 打印表格
	def print_form(self, form):
		for dic in form:
			# 移动到开始点位
			self.hDC.MoveTo((dic.get("x"), dic.get("y")))
			# 结束位置
			self.hDC.LineTo((dic.get("x1"), dic.get("y1")))

	# 数据处理
	def data_handle(self, data):
		'''
		拿到转成dict的数据，进行细分调用不同的接口打印
		'''
		# 获取打印机驱动名称
		# print(data)
		self.open_printer(data.get("Printername"))
		# 打印机配置
		self.setting_printer(data.get("PrinterSetting"))
		# 创建对象
		self.establish_pyCDC("filename", data.get("PrinterSetting"), data.get("Printername"))
		# 打印图片
		if data.get("Image") != None:
			self.print_image(data.get("Image"))

		# 打印文字
		if data.get("words") != None:
			self.print_words(data.get("words"))

		# 打印表格
		if data.get("form") != None:
			self.print_form(data.get("form"))
			
		self.hDC.EndPage()
		# 完成文件的假脱机并开始打印
		self.hDC.EndDoc()
		# 删除与设备上下文关联的所有资源
		self.hDC.DeleteDC()


	# 程序入口，接收json格式的数据
	def receive_json(self, jsondata):
		'''
		接收传递的json数据
		'''
		try:
			self.data_handle(jsondata)
		except Exception as e:
			print("错误输出",e)

def run(jsondata):
	printer = Printer()
	printer.receive_json(jsondata)


if __name__ == '__main__':
	printer = Printer()
	fp = open(BASE_DIR + "/Printing/LabelModel.json", "r", encoding='UTF-8')
	data = json.load(fp)
	fp.close()
	print(data)
	printer.receive_json(data)
