#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:


if (__name__ == "__main__"):
    age = int(input('Input your age: '))

    if age >= 18:
        print('adult')
    elif age >= 6:
        print('teenager')
    else:
        print('kid')

    weight=int(input(" Input your weight: "))

    if(weight>=100):
        print("肥")
    elif weight<=60:
        print("瘦")
    else:
        print("挺好")
