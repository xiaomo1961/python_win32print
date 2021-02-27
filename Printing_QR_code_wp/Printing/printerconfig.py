# _*_ coding:utf-8 _*_

'''
创建时间：2020-10-14
文件说明：打印机配置文件及说明
官方说明：http://timgolden.me.uk/pywin32-docs/PyDEVMODE.html
纸张尺寸设置：https://blog.csdn.net/lekonpeng/article/details/3078766
'''
import win32con


SpecVersion = win32con.DM_SPECVERSION               # type int  打印机规格版本  应始终设置为DM_SPECVERSION 默认

DriverVersion = 1024                                # type int 	打印机驱动版本  默认

Size = 220                                          # type int  结构尺寸  默认

DriverExtra = 1533                                  # type int  分配给驱动程序数据的额外字节数，只能在创建新对象时设置

Fields = win32con.DM_SPECVERSION                    # type int  win32con.DM_ *常量的位掩码，指示设置了哪些成员

Orientation = win32con.DMORIENT_LANDSCAPE           # type int  方向  仅适用于打印机DMORIENT_PORTRAIT或DMORIENT_LANDSCAPE

PaperSize = win32con.DMPAPER_A4                     # type int  纸张尺寸 如果设置了PaperWidth和PaperLength，则使用0，否则使用win32con.DMPAPER_ *常量

PaperLength = 40                                    # type int  纸张高度 单位mm毫米 模版设置

PaperWidth = 30                                     # type int  纸张宽度 单位mm毫米 模版设置

Position_x = 0                                      # type int  显示器相对桌面的位置 x

Position_y = 0                                      # type int  显示器相对桌面的位置 y

DisplayOrientation = win32con.DMDO_DEFAULT          # type int  显示方向：DMDO_DEFAULT，DMDO_90，DMDO_180，DMDO_270

DisplayFixedOutput = win32con.DMDFO_STRETCH         # type int  固定输出显示 DMDFO_DEFAULT，DMDFO_CENTER，DMDFO_STRETCH

Scale = 0                                           # type int  刻度 指定为百分比，例如50表示原始尺寸的一半

Copies = 0                                          # type int  副本 指定为百分比，例如50表示原始尺寸的一半

DefaultSource = None                                # type int  默认来源  DMBIN_ *常量，或者可以是打印机特定的值

PrintQuality = None                                 # type int  印刷质量  DMRES_ *常量，如果为正则解释为DPI

Color = win32con.DMCOLOR_COLOR                      # type int  颜色  DMCOLOR_COLOR或DMCOLOR_MONOCHROME

Duplex = win32con.DMDUP_SIMPLEX                     # type int  双工  对于进行双面打印的打印机：DMDUP_SIMPLEX，DMDUP_HORIZONTAL，DMDUP_VERTICAL

YResolution = None                                  # type int  DPI中的垂直打印机分辨率-如果设置，则PrintQuality指示水平DPI

TTOption = win32con.DMTT_BITMAP                     # type int  选项 TrueType选项：DMTT_BITMAP，DMTT_DOWNLOAD，DMTT_DOWNLOAD_OUTLINE，DMTT_SUBDEV

Collate = win32con.DMCOLLATE_TRUE                   # type int  整理  DMCOLLATE_TRUE或DMCOLLATE_FALSE

LogPixels = None                                    # type int  每英寸像素（仅适用于显示设备）

BitsPerPel = None                                   # type int  颜色分辨率（以每像素位数为单位）

PelsWidth = None                                    # type int  显示像素宽度

PelsHeight = None                                   # type int  显示像素高度

DisplayFlags = None                                 # type int  显示标志  DM_GRAYSCALE和DM_INTERLACED的组合

DisplayFrequency = None                             # type int  显示频率  

DisplayOrientation = None                           # type int  显示旋转 DMDO_DEFAULT，DMDO_90，DMDO_180，DMDO_270

ICMMethod = None                                    # type int  ICM方法  指示执行ICM的位置，是win32con.DMICMMETHOD_ *值之一

ICMIntent = None                                    # type int  ICM的意图，是win32con.DMICM_ *值之一

MediaType = None                                    # type int  媒体类型  win32con.DMMEDIA_ *，也可以是特定于打印机的值，大于DMMEDIA_USER

DitherType = None                                   # type int  抖动选项，win32con.DMDITHER_ *

Reserved1 = None                                    # type int  保留，仅使用0

Reserved2 = None                                    # type int  保留，仅使用0

Nup = None                                          # type int  控制每个物理页DMNUP_SYSTEM或DMNUP_ONEUP的多个逻辑页的打印

PanningWidth = None                                 # type int  未使用，保留为0

PanningHeight = None                                # type int  未使用，保留为0

DeviceName = None                                   # type str  设备名

FormName = None                                     # type str  由win32print :: EnumForms返回的表单名称，最多32个字符

DriverData = None                                   # type str  驱动程序数据附加到结构的末尾













