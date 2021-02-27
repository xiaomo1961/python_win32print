# _*_ coding:utf-8 _*_ 

'''
创建时间：2020-10-13
文件说明：pywin32 windows API 测试文档
'''

# 导入包
import win32print
import win32ui
import win32con
import win32api
from PIL import Image, ImageWin

TEXT = """公司名称：XXX科技有限公司
产品名称：老干妈
规格：XXX
数量：6瓶
型号：TDR1212Z
出厂日期：2020-10-12"""
TEXT = """公司名称：XXX科技有限公司"""
TEXT1 = """0"""
def windows_Api():
	# 检索打印机句柄
	# printer_drive_name = "EPSON LQ-630K ESC/P 2 Ver 2.0"
	# PyPrinterHANDLE = win32print.OpenPrinter(printer_drive_name, None)

	# 列出已安装的打印机驱动
	# drive = win32print.EnumPrinterDrivers()
	# print(drive)
	# 返回的是元祖，元祖中是dict value 是驱动的名称
	# win32print.AddForm  为打印机添加表单
	INCH = 1440
	# pywin32ui 创建PYCDC对象
	printer_name = win32print.GetDefaultPrinter()
	# 设置打印机参数
	# 打印机配置参数
	PyDEVMODE = {
		"PaperLength":1/10,
		"PaperWidth":1/10,
	}
	# 更改打印机配置
	'''
	参数

	'''
	# win32print.DocumentProperties()

	# attributes = win32print.GetPrinter(handle, level)
	pHandle = win32print.OpenPrinter(printer_name,{"DesiredAccess":win32print.PRINTER_ACCESS_USE})
	attributes = win32print.GetPrinter(pHandle, 2)
	# 打印机规格版本
	print(attributes["pDevMode"].SpecVersion)
	# 驱动版本
	print(attributes["pDevMode"].DriverVersion)
	# 结构尺寸
	print(attributes["pDevMode"].Size)
	# 驱动公司
	print(attributes["pDevMode"].DriverExtra)
	# 字段
	print(attributes["pDevMode"].Fields)
	# 方向
	print(attributes["pDevMode"].Orientation)
	print("+++++打印机配置参数+++++")
	attributes.get("pDevMode").PaperWidth = 400
	attributes.get("pDevMode").PaperLength = 300
	attributes.get("pDevMode").Orientation = 1
	# attributes.get("pDevMode").Orientation = win32con.DMORIENT_LANDSCAPE
	# 设置
	win32print.SetPrinter(pHandle, 2, attributes, 0) 
	print(attributes.get("pDevMode").PaperWidth)
	print(printer_name)
	hDC = win32ui.CreateDC()
	hDC.CreatePrinterDC(printer_name)
	# hDC = win32ui.CreateDC()

	# hDC.CreatePrinterDC(printer_drive_name)

	# 开始将文档假脱机保存到打印机DC (两个参数，1，文档名称，2，输出文件名。使用它来缓冲文件。忽略发送到打印机)
	hDC.StartDoc("test1")
	# 在打印机DC上启动一个新页面
	hDC.StartPage()
	# 设置设备上下文的映射模式
	# 映射模式 MM_ANISOTROPIC, MM_HIENGLISH, MM_HIMETRIC, MM_ISOTROPIC, MM_LOENGLISH, MM_LOMETRIC, MM_TEXT, MM_TWIPS
	hDC.SetMapMode (win32con.MM_ISOTROPIC)

	# 设置
	hDC.SetWindowExt((40, 30))

	# DrawText() 格式化给定矩形中的文本 参数(text,(0,0,0,0),win32con.DT_CENTER )  (0,INCH*-1,INCH*8,INCH*-2), 
	# text 文本（0，0，0，0）位置，分别是左，上，右，下， win32con.DT_CENTER, DT_CENTER :居中显示, DT_SINGLELINE :单行显示, DT_VCENTER:垂直居中显示 
	# hDC.DrawText("TSES", (0, INCH*-1, INCH*8,INCH*-2), win32con.DT_LEFT)
	# hDC.DrawText("HELLO\nHELLO", (0, INCH*-3, INCH*8,INCH*-4), win32con.DT_LEFT)
	# 打印文本
	# for y in range(5):
	# 	hDC.TextOut(0,INCH*-y,TEXT)
	# for x in range(5):
	# 	hDC.TextOut(INCH*4,INCH*-x, TEXT1)
	# hDC.TextOut(0,INCH*-4,TEXT)

	# 划线
	# 起始位置
	# for y in range(1,5):
	# 	# 移动当前点位
	# 	hDC.MoveTo((INCH*2,INCH*-y))
	# 	# print(d)
	# 	# 结束位置
	# 	hDC.LineTo((INCH*4,INCH*-y))
	# hDC.LineTo((100,INCH*6))
	# 用指定的纯色填充给定的矩形
	# hDC.FillSolidRect((10, -10, 100,-100),10)
	# 在DC打印机上完成一个页面
	# # 框架矩形
	# win32color = win32ui.CreateBrush()
	# s = hDC.SelectObject(win32color)
	# hDC.FrameRect((10, -10, 100, -100), s)
	# 改变字体大小和颜色 (字体大小搞定)
	'''
	字体设置参数 参数类型 dict
	height 字体高度
	width 字体宽度
	escapement  擒纵
	orientation  方向
	weight   重量
	italic   斜体
	underline  下划线
	strike out  删除
	charset   字符集
	out precision  精确的
	clip precision 剪辑精确的
	quality  质量
	pitch and family 音调和  
	name  字体名称
	'''
	# font = {
	# 	"height":2,             # 字体高度
	# 	"width":1,               # 字体宽度
	# 	"escapement":0,          # 擒纵
	# 	"orientation":0,         # 方向
	# 	"weight":False,          # 重量
	# 	"italic":False,          # 斜体
	# 	"underline":True,        # 下划线
	# 	"name":"宋体",           # 字体      
	# }
	# win32font = win32ui.CreateFont(font)
	# hDC.SelectObject(win32font)
	# hDC.TextOut(2, -5, TEXT)
	# hDC.TextOut(2, -28, "我是一个测试")

	# 打印图片
	# 打开图片并缩放
	# 纸张大小
	printable_area = (40, 30)
	bmp = Image.open("./code.png")
	if bmp.size[0] < bmp.size[1]:
		bmp = bmp.rotate(180)
	# ratios = [1.0 * printable_area[0] / bmp.size[1], 1.0 * printable_area[1] / bmp.size[0]]
	# scale = min(ratios)
	scale = 1
	# 打印二维码
	# hDC.StartDoc(img)
	# hDC.StartPage()

	dib = ImageWin.Dib(bmp)
	scaled_width, scaled_height = [int(scale * i) for i in bmp.size]
	print(scaled_width, scaled_height)
	print(scaled_width)

	x1 = 14  # 控制位置
	y1 = -2
	x2 = 40
	y2 = -28
	print(x1,x2,y1,y2)
	dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))


	hDC.EndPage()
	# 完成文件的假脱机并开始打印
	hDC.EndDoc()
	# 删除与设备上下文关联的所有资源
	hDC.DeleteDC()



if __name__ == '__main__':
	windows_Api()