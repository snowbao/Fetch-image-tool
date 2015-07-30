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
            print u'downloading pic%s now, please waiting' % x
            urllib.urlretrieve(i,temp)
            x+=1

source = getHtml('http://www.tooopen.com/img/87.aspx')
print getImage(source)