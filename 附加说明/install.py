#!/usr/bin/env python
#coding:utf8
import time
import logging

logging.basicConfig(level=logging.DEBUG,   
                    filename='d:\py_work\\test.txt',  
                    filemode='w') 
					 

with open('d:\py_work\\test.txt',"a+") as file:
	for i in xrange(1,20):
		time.sleep(1)
		info = 'testing.......!----%d'% (i)
		print info
		logging.info(info)
