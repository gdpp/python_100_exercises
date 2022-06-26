# Write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

import zlib

s = 'hello world!hello world!hello world!hello world!'
y = bytes(s, 'utf-8')
t = zlib.compress(y)
print(t)
print(zlib.decompress(t))