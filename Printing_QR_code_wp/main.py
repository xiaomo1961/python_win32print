# _*_ coding:utf-8 _*_

'''
创建时间：2020-10-21
文件说明：项目启动文件
'''


import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebChannel import QWebChannel
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from threading import Thread
from client import QR_code

# 异步调用函数装饰器
def async(func):
    def wrapper(*args, **kwargs):
        thr = Thread(target=func, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QR_code.LoginDialog()
    # window.show
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
	