# -*- coding:utf-8 -*-
#__author__ = Andor_ZZ

week = '星期一星期二星期三星期四星期五星期六星期日'
date = int(input('please enter date:'))
weekday = week[(date % 7 -1)*3:(date % 7 -1)*3+3]
print(weekday) 
