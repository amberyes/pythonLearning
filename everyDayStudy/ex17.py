from sys import argv
from os.path import exists
argv = ["ex15","ex16_sample.txt", "ex16_sampla.txt"]
script, from_file, to_file = argv
print "Copying from %s tp %s" % (from_file,to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready,hit  REUTRN tocontinue,CTRL-C to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "Alrigt,all done."

out_file.close()
in_file.close()