# _*_ coding:utf-8 _*_

'''
创建时间：2020-10-21
文件说明：释放端口
'''

import os
def killPort(port):
    # 查找端口的pid
    find_port= 'netstat -aon | findstr %s' % port
    result = os.popen(find_port)
    text = result.readline()
    pid= text.split()
    # pid = [] 说明端口没被占用
    if pid != []:
    	# 占用端口的pid
    	find_kill= 'taskkill -f -pid %s' %pid[4]
    	result = os.popen(find_kill)
    return result.read()

if __name__ == '__main__':
	killPort(8088)