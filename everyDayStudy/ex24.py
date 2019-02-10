# -*- coding:utf-8 -*-
print "Let's practice everything."
#\'表示单引号，\\表示单斜杠，\n表示换行，\t表示制表
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-------------------------------"
print poem
print "-------------------------------"

#five=5
five = 10-2+3-6
print "This should be five:%s"%five

#函数接受一个参数，返回三个值
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#解包，将secrect_formula(start_point)返回的三个值赋值给三个变量,用来存放
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d"% start_point
print "We'd have %d beans, %d jars,and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#secrect_formula(start_point)返回的三个值
print "We'd have %d beans, %d jars, and %d crates."%secret_formula(start_point)