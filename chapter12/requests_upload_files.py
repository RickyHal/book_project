# requests_upload_files.py
#!/usr/bin/env python3
import requests
file = {'file1': open('test1.txt', 'r'), 'file2': open(
    'test2.txt', 'r'), 'file3': open('test3.txt', 'r')}
res = requests.post('http://httpbin.org/post', files=file)
print(res.text)
