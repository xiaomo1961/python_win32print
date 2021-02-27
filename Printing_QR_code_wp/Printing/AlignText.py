# _*_ coding:utf-8 _*_ 

'''
创建时间：2020-10-20
文件说明：设置打印文本的对齐方式
'''
import win32con

TextAlign = {
	"TA_CENTER": win32con.TA_CENTER,                     # 基准点与限定矩形的中心水平对齐。
	"TA_LEFT": win32con.TA_LEFT,                         # 基准点在限定矩形的左边界上。
	"TA_RIGHT": win32con.TA_RIGHT,                       # 基准点在限定矩形的右边界上。
	"TA_BASELINE": win32con.TA_BASELINE,                 # 基准点在正文的基线上。
	"TA_BOTTOM": win32con.TA_BOTTOM,                     # 基准点在限定矩形的下边界上。
	"TA_TOP": win32con.TA_TOP,                           # 基准点在限定矩形的上边界上。
	"TA_NOUPDATECP": win32con.TA_NOUPDATECP,             # 每次文字输出调用后当前基准点不改变。基准点是传输给正文输出函数的位置。
	"TA_UPDATECP": win32con.TA_UPDATECP,                 # 每次文字输出调用后当前基准点改变。当前位置作为基准点。
}