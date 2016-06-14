"""
    File Name:      FindDuplicates.py
    Type:           Python
    Description:    This file is for finding the duplicates files and
                    list them out.
"""

## Importing all the libraries
from os import walk
import re # Regular Expression
from subprocess import Popen, PIPE
import subprocess
import os
from collections import Counter

def list_duplicates(seq):
	seen = set()
	seen_add = seen.add
	# adds all elements it doesn't know yet to seen and all other to seen_twice
	seen_twice = set( x for x in seq if x in seen or seen_add(x) )
	# turn the set into a list (as requested)
	print seen
	print seen_twice
	print seen_add
	return list( seen_twice )


cmd = "find ~/SCRIPTS -type f | xargs md5"
p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
filelist = dict()
filelistWithPath = dict()

## Check for Error Code
#print "Return code: ", p.returncode
#print "Error: ", err.rstrip()
#print out.rstrip(), err.rstrip()
lines = out.rstrip().split("\n")

## Traverse the output
for line in lines:
    #print "Line : >>>", line
    matchObj = re.match(r'MD5 \((.*)\) = (.*)', line, re.M|re.I)
    if matchObj:
        #print "matchObj.group() : >>>", matchObj.group()
        head, tail = os.path.split(matchObj.group(1))
        #print "File Name: ", tail
        #print "File Path:  ", head
        #print "MD5 : ", matchObj.group(2)
	filelist[matchObj.group(2)] = tail
	filelistWithPath[matchObj.group(2)] = head
    else:
        print "No match!!"

keys = filelist.keys()
values = filelist.values()

print
print filelist
print len(filelist)
print keys
print values 
print list_duplicates(keys) # yields [1, 2, 5]
