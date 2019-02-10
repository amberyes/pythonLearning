def print_two(*args):
    arg1, arg2,arg3 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing."


print_two("Amber","s","Ye")
print_two_again("amber","Yes")
print_one("JJ")
print_none()