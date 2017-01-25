#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：

# 如果.py文件本身使用UTF-8编码，并且也申明了# -*- coding: utf-8 -*-，打开命令提示符测试就可以正常显示中文：



# =========================================================================================
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['javascript', 'web', 'php', 'java', 'python']
# print(classmates)
# 用len()函数可以获得list元素的个数：
# print(len(classmates))
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
# print(classmates[0])
# print(classmates[1])
# print(classmates[2])
# print(classmates[3])
# print(classmates[4])
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
# print(classmates[-1])                           # 倒数第一个
# print(classmates[-2])                           # 倒数第二个



# =========================================================================================
# append  往list中追加元素到末尾：    【append】
# classmates.append('css3')
# print(classmates[len(classmates)-1])
# classmates.append('html5')
# print(classmates[len(classmates)-1])



# =========================================================================================
# 元素插入到指定的位置，比如索引号为1的位置：    【insert】
classmates.insert(1, '这个是insert添加的')
print(classmates)

























