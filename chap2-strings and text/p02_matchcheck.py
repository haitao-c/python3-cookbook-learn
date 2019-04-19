"""
检查字符串开头或结尾是否匹配
"""
import re
import os
from urllib.request import urlopen


def start_end():
    filename = 'spam.txt'
    print(filename.endswith(".txt"))
    print(filename.startswith('file:'))
    url = 'http://www.python.org'
    print(url.startswith('http:'))

    filenames = os.listdir('.')
    print([name for name in filenames if name.endswith('.py')])
    # any内置函数: 只要有迭代集合中有一个元素满足条件就返回True
    print(any(name.endswith('.py') for name in filenames))

    choices = ['http:', 'ftp:']
    url = 'http://www.python.org'
    url.startswith(tuple(choices))

    # 正则表达式实现
    url = 'http://www.python.org'
    # re.match()返回一个匹配对象
    m = re.match(r'http:|https:|ftp:', url)
    # m.group()返回被RE匹配的字符串
    print(m.group())


if __name__ == '__main__':
    start_end()
