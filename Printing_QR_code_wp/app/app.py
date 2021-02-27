# _*_ coding:utf-8 _*_

'''
创建时间：2020-10-10
文件说明：接口程序
'''
import sys
import os
import json
import time
import datetime
import configparser
from flask import Flask, redirect, url_for, make_response
from flask import jsonify
from flask import request
from flask_cors import CORS
from gevent import pywsgi
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from app.get_hostIp import *
from app.kill_port import *
# import get_hostIp
from Printing.printerprogram import *
printer = Printer()
conf = configparser.ConfigParser()
conf.read(BASE_DIR + '/config/config.ini')  # 文件路径
host = conf.get('apiserver', 'host')
port = conf.get('apiserver', 'port')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, resources=r'/*')

datec = datetime.datetime(2030,11,10,0,0,0)
timestamp = int(time.mktime(datec.timetuple()))
# 获取当前时间戳
def time_stamp():
	stamp = int(time.time())
	return stamp

# 程序过期时间,
def be_overdue():
	if timestamp >= time_stamp():
		return True
	else:
		return False

# 写入token数据
def save_data(data):
	with open(BASE_DIR + '/config/token.txt', 'w', encoding='utf8') as f:
		f.write(data)
		f.close()

@app.route('/Printing_code', methods = ['POST', 'GET'])
def Printing_code():
	# 判断程序是否过期

	try:
		# print(request.form)
		# box_type = request.form['box_type']
		# box_num = request.form['box_num']
		# print_num = request.form['print_num']
		data = request.get_data()
		jsondata = json.loads(str(data, encoding="utf8"))
		content = {"code": 200, "msg": "正在打印"}
		# 调用打印机程序
		run(jsondata)
	except Exception as e:
		print(e)
		content = {"code": 400, "msg": "参数错误"}
	return jsonify(content)

@app.route('/SaveData', methods = ['POST', 'GET'])
def SaveData():
	try:
		data = request.get_data()
		jsondata = json.loads(str(data, encoding="utf8"))
		save_data(str(jsondata.get("uniacid")))
		content = {"code":200, "msg": "保存成功"}
	except Exception as e:
		content = {"code": 400, "msg": "保存失败"}
	return jsonify(content)



@app.route('/play', methods = ['POST', 'GET'])
def play():
	return jsonify({"code":200, "num":2})

def runserver():
    killPort(int(port))
    server = pywsgi.WSGIServer((host, int(port)), app)
    # app.run(HOST, port=POST, debug=False)
    server.serve_forever()
runserver()

if __name__ == '__main__':
   app.run('192.168.1.131',8088, debug = True)