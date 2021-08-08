
import requests
import random
import wget

def GetARandomJpgName():
    rand_int = random.randint(1,10000)
    rand_char = random.choice("NotToday")
    return str(rand_char)+str(rand_int)+".jpg"

def IsImageResponse(content):
    http_response = ["head","body"]
    for html_content in http_response :
        html_content = bytes(html_content, encoding = "utf8")
        if content.find(html_content) ==-1:
            return True
    return False

def GetRequestContent(address,payload=""):
    headers = requests.utils.default_headers()
    headers.update(
    {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    })
    r = requests.get(address,headers=headers)
    print(address,payload,r.content.decode())
    return r.content

def DownloadPic(address,name):
    content = wget.dow
    with open(name, "wb") as f:
        f.write(content)
        return True
# api ref： https://github.com/TimothyYe/bing-wallpaper
# https://bing.biturl.top/?resolution=1920&format=json&index=0&mkt=zh-CN ,获取当天的bing壁纸

# https://bing.biturl.top/?resolution=1920&format=json&index=0&mkt=zh-CN
today_pic_api = "https://bing.biturl.top/?resolution=1920&index=0&mkt=zh-CN"
bing_pic_api = "https://bing.biturl.top"
def GetBingBgUrl(index):
    payload = {'resolution': '1920', 'format': 'json','index':str(index),'mkt':'zh-CN'}
    content = GetRequestContent(today_pic_api)
    # ret = os.system("wget '"+today_pic_api+"'")
    print(content.decode())
    if len(content)!=0:
        return content["url"]
    return ""
import os
import time
def main():
    print(os.listdir("./"))
    if not "bing_bg" in os.listdir("./"):
        os.makedirs("./bing_bg/")
    print(GetBingBgUrl('1'))

if __name__ == "__main__":
    main()