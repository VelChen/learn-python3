#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

print("o==========0")

lea = [x * x for x in range(1, 4)]
print(lea)

leb = [x * x for x in range(1, 10) if (x % 2 == 0)]
print(leb)

lec = [str(x) + str(y) for x in range(10) if (x % 2 == 0) for y in range(10) if (y % 2 > 0)]
print(lec)

if (__name__ == "__main__"):
    pass
