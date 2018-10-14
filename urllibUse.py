
#urllib.request 的使用
# request 请求 get类型
"""
import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read())
"""

#urllib.parse 的使用
# urllib.request.urlopen(url,data=None,[timeout,]* m cafile = None , cadefault = False , context= None )
# parse post类型  (此处如果data不加到请求的参数里，那么请求类型就是get，如果加data，类型就是post)
"""
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data = data )
print(response.read())
"""

# 超时设置
"""

import urllib.request
response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
print(response.read()) #read 方法是获取响应体内容 字节流型的数据 ,需要使用utf-8解码

"""

"""

# 异常设置
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
"""

#响应
#响应类型
"""

import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(type(response))

"""

#响应头
"""

import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
print(response.status)
print(response.getheaders()) #响应头
print(response.getheader('Server'))
print(response.getheader('Date'))

"""
#发送的请求中包含自定义参数的情况，注意,urllib.request.urlopen 的参数列表中，是无法加入自定义的参数的
"""
import urllib.request
request = urllib.request.Request("http://www.baidu.com")
response = urllib.request.urlopen(request)
print(response.read())
"""

"""

from urllib import request,parse
url = 'http://httpbin.org/post'
headers = {
     'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
     'Host':'httpbin.org'
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url = url , data = data , headers = headers , method= 'POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
"""

#向request 请求头中添加参数
"""
from urllib import request,parse

url = 'http://httpbin.org/post'
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url = url , data = data , method = 'POST')
req.add_header('User-Agent','Mozilla/4.0(compatilble;MSIE 5.5; Windows NT)')
#如果向在请求头中添加多个参数，可以一个一个的赋过来
response = request.urlopen(req)
print(response.read().decode('utf-8'))
"""
"""

#Url 有很多handler ，api文档里有
#代理handler
#这段代码在本机上测试没有成功
#可以使用代理，避免多次请求同一个网址，被封IP
import urllib.request

proxy_headler = urllib.request.ProxyHandler({
    'http':'http://96.45.191.50:443',
    'https':'https://96.45.191.50:443'
})
opener = urllib.request.build_opener(proxy_headler)
response = opener.open('http://www.baidu.com')
print(response.read())
"""


"""
#cookieHandler
#爬虫里面，cookie的作用是保持登录状态

import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)
"""
"""
#urlparse 解析
# urllib.parse.urlparse(urlstring,scheme='', allow_fragments= True)

from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#commnet')
print(type(result),result) #将url进行拆分
"""

"""

from urllib.parse import urlparse

result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme= 'https')
print(result) #第二个参数是协议类型
"""

"""
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html;user:id=5#comment',scheme='https')
print(result)#第二个参数不会生效
"""

"""
from urllib.parse import urlparse

result = urlparse('www.baidu.com/index.html;user?id=5#comment',allow_fragments=False)
print(result)#输出的结果，将fragment 拼接到query中了,向前拼接
"""

"""
#urlunparse
#将url进行拼接
from urllib.parse import urlunparse

data = ['http','www.baidu.com','index.html','user','a=6','commnet']
print(urlunparse(data))
"""

#urljoin
#将两个url进行拼接

"""
#urlencode
#把一个字典对象转换成get请求参数
from urllib.parse import urlencode
params = {
    'name':'germey',
    'age':22
}
base_url = 'http://www.baidu.com?'
url = base_url+urlencode(params)
print(url)
"""



