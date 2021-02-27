# _*_ coding:utf-8 _*_

'''
创建时间：2020-10-21
文件说明：获取本机的ip
'''
import socket

# 查询本机的ip
def get_host_ip():
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		sock.connect(('8.8.8.8',80))
		ip = sock.getsockname()[0]
	finally:
		sock.close()

	return ip

if __name__ == '__main__':
	print(get_host_ip())