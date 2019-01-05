from urllib import request
import urllib
import re
import time
def get_html(httpUrl):
	page = urllib.request.urlopen( httpUrl )
	htmlCode = page.read( )
	return htmlCode

def download_pic(address,name):    
	urllib.request.urlretrieve(address, name)

local = time.strftime("%Y.%m.%d")
url = 'http://cn.bing.com/'
html_code=get_html(url)
html_str=html_code.decode(encoding = "utf-8")

reg = r"(az/hprichbg/rb/.*?.jpg)"

add = re.findall(reg, html_str, re.S)[0]

picUrl = url + add
download_pic(picUrl,"%s.jpg" %local)# 在%s前面加上本地地址即可，默认为当前目录下
print("Successful Download")
