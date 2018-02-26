import urllib.request
import re
from lxml import etree


# proxylist=[
#     {"http":"180.117.97.43:808"},
#     {"http":"218.68.99.69:8118"},
#     {"http":"221.3.39.207:8118"},
#     {"http":"112.229.233.179:8118"},
    
# ]
# proxy=random.choice(proxylist)
# #代理处理器的对象
# urllib.request.ProxyHandler(proxylist)

# handler=urllib.request.ProxyHandler(proxy)

# opener=urllib.request.build_opener(handler)

# req=urllib.request.Request("http://www.baidu.com")
# response=opener.

# info="<a href="http://www.baidu.com">baidu</a>"

# obj=re.compile("[a-z.]*baidu[a-z.]*")
# result=obj.findall(info)
# print(result)

class xiaohua():
    def __init__(self,page):
        self.page=page
        self.status=True
    
    def loadpage(self):
        url="http://www.neihanpa.com/article/index_"+str(self.page)+".html"
        if self.page==1:
            url="http://www.neihanpa.com/article/index.html"

        ua_headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        req=urllib.request.Request(url,headers=ua_headers)
        response=urllib.request.urlopen(req)
        html=response.read().decode('utf-8')
        
        obj=re.compile('<div class="desc">(.*?)</div>') 
        content=obj.findall(html)
        self.dealdata(content)
    

    def dealdata(self,content):
        for item in content:
            item=item.replace("\u3000","")
            self.savedata(item)

    def savedata(self,item):
        print(item)
        with open("xiaohua.txt","a") as f:
            f.write(item)
            f.write("\n")       

    def startwork(self):
        while self.status:
            self.loadpage()
            result=input("go on?y/n")
            if result=="n":
                self.status=False
            self.page=self.page+1
        print("谢谢使用")
 
spilder=xiaohua(1)
spilder.startwork()