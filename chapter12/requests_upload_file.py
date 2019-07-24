# requests_upload_file.py
#!/usr/bin/env python3
import requests
file = {'file': open('test.txt', 'r')}
res = requests.post('http://httpbin.org/post', files=file)
print(res.text)
