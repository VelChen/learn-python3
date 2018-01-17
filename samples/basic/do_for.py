#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印list:

from collections import Iterable, Iterator, Generator

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 打印数字 0 - 9
for x in range(10):
    print(x)


z =[ x*x for x in range(10)]

print(isinstance(z,Iterable))

zx =(x*x for x in range(5))
print(isinstance(zx,Generator))


if(__name__=="__main__"):
    pass