from sys import argv


argv = ["ex15", "ex15_sample.txt"]

script, filename = argv

txt = open(filename)

print "Here's your file %s:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
txt.close()