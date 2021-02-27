# import labels
# from reportlab.graphics import shapes
 
# specs = labels.Specification(210, 297, 2, 8, 90, 25, corner_radius=2)
 
# def draw_label(label, width, height, obj):

# 	label.add(shapes.String(2, 2, str(obj), fontName="Helvetica", fontSize=40))
	 
# # Create the sheet.
# sheet = labels.Sheet(specs, draw_label, border=True)
 
# # Add a couple of labels.
# sheet.add_label("Hello")
# sheet.add_label("World")
 
# # We can also add each item from an iterable.
# sheet.add_labels(range(3, 22))
 
# sheet.add_label("Oversized label here")
 
# # Save the file and we are done.
# sheet.save('basic.pdf')
# print("{0:d} label(s) output on {1:d} page(s).".format(sheet.label_count, sheet.page_count))


# # _*_ coding:utf-8 _*_

# '''
# 创建时间：2020-10-10
# 文件说明：调用打印机，打印条码和二维码
# '''

# import win32print
# import win32ui
# import win32con

# text = """
# 公司名称：XXX有限公司
# 产品名称：老干妈
# 规格：XXX
# 数量：6瓶
# 型号：TDR1212Z
# 出厂日期：2020-10-12
# """

# def print2Printer():
#     INCH = 1440

#     hDC = win32ui.CreateDC ()
#     hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
#     hDC.StartDoc ("Test doc")
#     hDC.StartPage ()
#     hDC.SetMapMode (win32con.MM_TWIPS)
#     hDC.DrawText (text, (0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)
#     hDC.EndPage ()
#     hDC.EndDoc ()
# print2Printer()

import datetime
import png
import win32con

# # 打印二维码
def print_barcode():
    import pyqrcode
    import random,string
    from PIL import Image,ImageDraw,ImageFont
    import numpy as np
    # if request.is_ajax() and request.method == 'POST':
    result = {}
    #     bar_string = 'NaN'
    #     type = request.POST['type']

    #     if type == 'box':
    #         # 生成箱子码
    #         # 格式：P190823-K91  [P][日期][-][A-Z][0-9][0-9]
    bar_string = 'P'+datetime.date.today().strftime('%y%m%d')+'-'+str(random.choice('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))\
                 + str(random.choice(range(10)))+ str(random.choice(range(10)))
        # elif type == 'kuwei':
        #     # 生成库位码
        #     bar_string = request.POST['string']
        # else:
        #     pass

    # try:
    big_code = pyqrcode.create(bar_string, error='L', version=2 , mode='binary')
    big_code.png('./code.png', scale=8)
    img_code = Image.open('code.png')

    size = img_code.size
    img_final = Image.new('RGB', (size[0], size[1]+35), color=(255, 255, 255))
    img_final.paste(img_code, (0, 0, size[0], size[1]))

    draw = ImageDraw.Draw(img_final)
    font = ImageFont.truetype('AdobeGothicStd-Bold.otf', size=35)
    width, height = draw.textsize(bar_string,font=font)
    draw.text(((size[0]-width)/2, size[1]-15), bar_string , fill=(0, 0, 0), font=font)
    img_final.save('./code.png')

    # 然后连接打印机将其打印出来即可
    is_ok =[]
    if type == 'box':
        for i in range(4):
            temp = print_img('./code.png')
            is_ok.append(temp)
    else:
        temp = print_img('./code.png')
        is_ok.append(temp)
    # is_ok = True
    result['done'] = 'ok' if np.all(is_ok) else '连接打印机失败'
    # except Exception as e:
    #     print(e)
    #     result['done'] = e

    # return JsonResponse(result)
 
def print_img(img):
    import win32print
    import win32ui
    import win32con
    from PIL import Image, ImageWin
    INCH = 1440
    # 参考 http://timgolden.me.uk/python/win32_how_do_i/print.html#win32print
    try:
	    printer_name = win32print.GetDefaultPrinter()
	    hDC = win32ui.CreateDC()
	    hDC.CreatePrinterDC(printer_name)

	    printable_area = (40, 30)  # 打印纸尺寸
	    # printer_size = (25, 25)

	    # 打开图片并缩放
	    bmp = Image.open(img)
	    if bmp.size[0] < bmp.size[1]:
	        bmp = bmp.rotate(90)

	    ratios = [1.0 * printable_area[0] / bmp.size[1], 1.0 * printable_area[1] / bmp.size[0]]
	    scale = min(ratios)
	    scale = 1
		# 打印二维码
	    hDC.StartDoc(img)
	    hDC.StartPage()

	    dib = ImageWin.Dib(bmp)
	    scaled_width, scaled_height = [int(scale * i) for i in bmp.size]
	    print(scaled_width, scaled_height)
	    print(scaled_width)

	    x1 = 10  # 控制位置
	    y1 = -20
	    x2 = x1 + scaled_width
	    y2 = y1 + scaled_height
	    dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))

	    # hDC.EndPage()
	    # hDC.EndDoc()
	    # hDC.DeleteDC()
	    # 打印文字
	    # hDC.StartDoc("打印文字")
	    # hDC.StartPage()

	    # # hDC.DrawText("公司名称：xxx有限公司")
	    # hDC.SetMapMode (win32con.MM_TWIPS)
	    # # hDC.DrawText('ABC',(0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_LEFT)
	    # hDC.DrawText('你好',(1, INCH * -1, INCH * 8, INCH * -2), win32con.DT_LEFT)
	    hDC.EndPage()
	    hDC.EndDoc()
	    hDC.DeleteDC()

	    return True
    except Exception as e:
        print(e)
        return False
print_barcode()
# print_img('./code.png')
