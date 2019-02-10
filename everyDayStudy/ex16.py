# -*- coding: utf-8 -*-
from sys import argv

argv = ["ex15", "ex15_sample.txt"]
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that,hit CTRL-C(^C)."
print "If you do want that,hit RETURN."
print "input your line..."
raw_input("?")

#打开文件，赋予'写'操作
print "Opening the file..."
target = open(filename, 'w')

#清空文本内容
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#执行'写'操作
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#关闭文件
print "And finally, we close it."
target.close()