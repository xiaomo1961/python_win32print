# _*_ coding:utf-8 _*_

'''
创建时间：2020-10-26
文件说明：生成条形码
'''

import os
import time
import sys
from pystrich.code128 import Code128Encoder
from pystrich.ean13 import EAN13Encoder
from pystrich.qrcode import QRCodeEncoder


def code128(code):
    encoder = Code128Encoder(code,options={
        "ttf_font":"C:/Windows/Fonts/SimHei.ttf",
        "ttf_fontsize":24,
        "bottom_border":15,
        "height":170,
        "label_border":2
        })
    encoder.save("../static/code/bar_code.png", bar_width=4)
        


if __name__ == "__main__":
    code = "1234567891011"
    code128(code)
    # ean13()
    # qrcode()