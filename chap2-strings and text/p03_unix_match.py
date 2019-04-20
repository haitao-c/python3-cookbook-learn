from fnmatch import fnmatch, fnmatchcase

# 使用unix中的通配符作为表达式进行匹配判断

def unix_match():
    print(fnmatch('foo.txt', '*.txt'))  # * 表示字符可以不出现，也可以出现一次或多次
    print(fnmatch('foo.txt', '?oo.txt'))  # ? 表示前面的字符最多只可以出现一次(0或1次)
    print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print(name for name in names if fnmatch(name, 'Dat*.csv'))

    # 处理普通文本
    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]
    print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
    print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])


if __name__ == '__main__':
    unix_match()
