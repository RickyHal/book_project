# requests_json.py
#!/usr/bin/env python3
import json
import requests
# 获取成都天气预报
res = requests.get('https://www.apiopen.top/weatherApi', params={'city': '成都'})
print('API返回的内容：', res.text)
# 将返回的字符串转换为json对象，之后便可以使用获取字典内容的方法获取到想要的内容
data = json.loads(res.text)
print('城市：', data['data']['city'])
print('当前温度：%s摄氏度' % data['data']['wendu'])
