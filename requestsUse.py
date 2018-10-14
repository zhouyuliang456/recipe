#requests 库比urllib库要方便

"""
import requests

response = requests.get('https://www.baidu.com')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.cookies)
"""

"""
#request 的各种请求方式
import requests
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')
"""

"""
import requests

#基本get请求
response = requests.get('http://httpbin.org/get')
print(response.text)
"""


"""
#带参数的get请求
import requests

#response = requests.get('http://httpbin.org/get?name=germey&age=22')
data = {
    'name':'germy',
    'age' : '22'
}
response = requests.get('http://httpbin.org/get',params=data)
print(response.text)
"""

"""
#json解析
import  requests
import json
response = requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))
"""

"""

#解析二进制文件 (图片 视频等)
import requests

response = requests.get('https://github.com/favicon.ico')
print(type(response.text),type(response.content))
print(response.text)
print(response.content)
with open('favicon.ico','wb')as f:
    f.write(response.content)
    f.close()

"""

"""
#添加headers,访问有些网站的时候，如果没有加headers，会被拒绝访问

import requests  #对比下面这个例子
response = requests.get('https://www.zhihu.com/explore')
print(response.content)
"""

""" 
import requests

headers = {
      'User-Agent': 'Mozilla/5.0(Machinetosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML,like Gecko) Chrome /52.0.2743.116 Safari/537.36'
}
response = requests.get('https://www.zhihu.com/explore',headers = headers)
print(response.text)

"""

""" 

#基本的post请求
import requests
data = {'name':'germey','age':'22'}
headers = {
    'User-Agent': 'Mozilla/5.0(Machinetosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36(Kit/537.36(KHTML,like Gecko) Chrome /52.0.2743.116 Safari/537.36'
}
response = requests.post('http://httpbin.org/post',data= data,headers= headers)
print(response.json())
"""

""" 
#响应
import requests  #注意一下 requests的get方法在api文档里搜不到
response = requests.get('http://www.jianshu.com')
#print(response.status_code,response.content,response.cookies,response.url)
exit() if not response.status_code == 200 else print('Request Successfully')

#能够将回复的结果直接输出，比较方便
"""

"""

#状态码
import requests
response = requests.get('http://www.baidu.com')
# exit() if not response.status_code == 200 else print('request successfully')
exit() if not response.status_code == requests.codes.ok else print('request successfully')
"""



"""

#文件上传
import requests
files = {'file' : open('favicon.ico','rb')}
response = requests.post('http://httpbin.org/post',files = files)
print(response.text)
"""
