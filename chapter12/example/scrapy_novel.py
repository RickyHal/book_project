# scrapy_novel.py
#!/usr/bin/env python3
import requests
import os
import re
from fake_useragent import UserAgent
# User-Agent池
USER_AGENT = UserAgent()
# 首页
HOST = 'http://www.xbiquge.la'


# 爬取小说
class ScrapyOne(object):

    def __init__(self, book_link):
        super(ScrapyOne, self).__init__()
        # 小说链接
        self.book_link = book_link
        # 小说书名
        self.book_name = None

    # 爬取每章的链接
    def scrapy_chaper_link(self):
        try:
            # 随机生成请求头
            header = {"User-Agent": USER_AGENT.random}
            res = requests.get(self.book_link, headers=header)
            # 设置网页编码
            res.encoding = 'utf-8'
            # 通过正则表达式获取书名
            self.book_name = re.findall('<h1>(.*?)</h1>', res.text)[0]
            for item in re.findall(r'<dd>(.*?)</dd>', res.text):
                # 获取章节链接及章节名
                data = re.findall(r'<a href=(.*?)>(.*?)</a>', item)[0]
                chaper_link, chaper_name = HOST + data[0].replace("'", '').replace(" ", ''), data[
                    1].strip("")
                # 交与scrapy_text方法爬取章节内容
                self.scrapy_text(chaper_name, chaper_link)
        except Exception as e:
            print(e)

    # 爬取一章的内容
    def scrapy_text(self, chaper_name, chaper_link):
        try:
            header = {"User-Agent": USER_AGENT.random}
            res = requests.get(chaper_link, headers=header)
            res.encoding = 'utf-8'
            texts = []
            # 获取章节内容
            for item in re.findall(r'<div id="content">(.*?)<p>', res.text):
                # 清洗内容
                text = item.replace('<br />', '').replace('&nbsp;', '')
                if text:
                    texts.append(text)
            # 保存章节内容
            self.save(chaper_name, texts)
        except Exception as e:
            print(e)

    # 保存一章的内容
    def save(self, chaper_name, texts):
        try:
            # 文件夹不存在则以小说名字创建
            if not os.path.exists('./' + self.book_name):
                os.makedirs('./' + self.book_name)
            with open('./%s/%s.txt' % (self.book_name, chaper_name), 'a', encoding='UTF-8-sig') as f:
                f.write('%s\t\n\n' % chaper_name)
                for text in texts:
                    f.write(text + '\n')
            f.close()
            print(self.book_name, chaper_name, '保存成功')
        except Exception as e:
            print(self.book_name, chaper_name, '保存失败')

    def main(self):
        self.scrapy_chaper_link()


if __name__ == "__main__":
    # 小说的链接
    book_link = 'http://www.xbiquge.la/15/15409/'
    one = ScrapyOne(book_link)
    one.main()
