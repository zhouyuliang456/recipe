import requests
import re

content = requests.get('http://www.haodou.com/recipe/1215105/').text
pattern = re.compile('<dd.*?src="(.*?)".*?<em>(.*?)</em>(.*?)<', re.S)
results = re.findall(pattern, content)
for result in results:
    url , step , content = result
    print(url,step,content)

print('程序执行结束')