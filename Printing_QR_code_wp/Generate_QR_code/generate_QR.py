# _*_ coding:utf-8 _*_

'''
创建时间：2020-10-21
文件说明：生成不带图片的二维码
'''
import qrcode
from PIL import Image, ImageDraw


def create_code(url, file_name, save_path):
    qr = qrcode.QRCode(
        version=2,
        # 设置容错率为最高
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=8,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    # 把RGB的图转换成RGBA模式，处理alpha透明通道（后边替换透明为白色）
    w, h = img.size
    # 白底图
    white_img = Image.new("RGBA", (w + 6, h + 6), (255, 255, 255))
    # 粘贴白图
    img.paste(white_img, (w - 2, h - 2), white_img)
    save_file = save_path + file_name + '.png'
    img.save(save_file, quality=100)
    # img.show()
    return save_file

if __name__ == '__main__':
    save_path = r'D:\Printing_QR_code_ql\static\code'
    create_code('http://www.wupin.shop/security/oB3E89MaDjOJquI7UE', 'cs', save_path)