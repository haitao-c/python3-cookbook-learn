def r_text():
    # 迭代读取文件中的每行
    # with open()会在操作完毕后自动关闭文件
    with open('a.txt', 'rt') as f:  # r表示读, t表示文本模式
        for line in f:
            print(line)


def w_text():               # wt 模式下, 若没有文件则会自动创建该文件
    with open('a.txt', 'wt') as f:
        f.write('text1')
        f.write('text2')    # 写在同一行


if __name__ == '__main__':
    w_text()
    r_text()
