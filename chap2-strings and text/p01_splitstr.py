import re


def join_test():
    # join(slice) 将传进的slice切片中的元素按'字符'.join(slice)中的字符拼接成一个string
    a = ['1', '2']
    b = ['3', '4']
    print(';'.join(a))  # 1;2


def zip_test():
    a = ['1', '2']
    b = ['3', '4']
    for x, y in zip(a, b):  # zip(a,b)为元组列表即[(1,3),(2,4)]
        print(x + y)
        # 1 3
        # 2 4


def split_str():
    line = 'asdf fjdk; afed,fjek, asdf, foo'
    # 根据正则表达式中的符号: [;,\s]\s* (;或,或空格或他们之中的某个出现后又跟上若干空格)分割字符串
    print(re.split(r'[;,\s]\s*', line))  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
    # 使用了捕获分组, 被匹配的文本也出现在结果列表中
    print(re.split(r'(;|,|\s)\s*', line))  # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
    fields = re.split(r'(;|,|\s)\s*', line)
    values = fields[::2]
    print(values)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
    delimiters = fields[1::2] + ['']
    print(delimiters)  # [' ', ';', ',', ',', ',', '']
    print(''.join(v + d for v, d in zip(values, delimiters)))


if __name__ == '__main__':
    split_str()
    # join_test()
    # zip_test()
