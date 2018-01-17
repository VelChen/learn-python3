#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# type()

print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))

class Coder(object):
    def code(self):
        print("i can code ")
coder =Coder()
print("type(coder)",type(coder))
import types

print('type(\'abc\')==str?', type('abc')==str)

if __name__ == '__main__':
    pass