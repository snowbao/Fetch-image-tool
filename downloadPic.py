#!/usr/bin/python
#encoding=utf-8
import re
import os
import urllib

def getHtml(url):
    html = urllib.urlopen(url)
    scode = html.read()
    return scode

def getImage(source):
    filepath=os.getcwd()+'/pythonimg'
    if os.path.exists(filepath) is False:
        os.mkdir(filepath)
    reg = r'src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    images = re.findall(imgre,source)
    x = 0
    for i in images:
            temp = filepath + '/%s.jpg' % x
            print u'正在下载第%s张图片' % x
            urllib.urlretrieve(i,temp)
            x+=1

source = getHtml('http://www.5442.com/tag/rosi.html')
print getImage(source)