#!/usr/bin/python
import sys
import binascii

s = sys.argv[1]
n = len(s)
clean = []
for i in range(n):
 clean = hex(ord(s[i]))[2:4]
for i in range(n):
 clean = hex(ord(s[i]))[2:4]
 print(clean,end='')
