#下面是使用python提供的库，来驱动谷歌浏览器
from selenium import webdriver
from urllib import request
import requests
driver = webdriver.Chrome('/Users/zhouyuliang/Downloads/chromedriver')
driver.get('http://www.haodou.com/recipe/7012482/')
#驱动文件 放在下载目录中了，在webdriver.Chrome 后面引入一下就可以调用 谷歌浏览器进行自动化测试
print(driver.page_source) #使用driver.page_source 得到的网页源代码是经过浏览器后台 Ajax渲染后的，这个源代码才是我们想要的

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

response = request.urlopen("http://www.haodou.com/recipe/7012482/")
html = response.read()
print(html) # 使用 这种直接访问的方式，得到的源代码 是没有经过渲染的，不是我们最终想要的代码，我们最终要的代码是经过渲染的，这样才可以进行数据分析