def print_tofile():
    with open('a.txt', 'at')as f:       # at, 以文本方式打开, 并追加内容; wt 会覆盖原来的内容
        print('Hello World!', file=f)


if __name__ == '__main__':
    print_tofile()
