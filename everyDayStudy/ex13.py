# -*- coding: utf-8 -*-
from sys import argv

argv = ["ksj", "2", "3", "4"]
#将argv解包：把argv中的东西解包，将所有的参数依次复制给左边的这些变量
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
