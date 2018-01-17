#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = (x * x for x in range(5))  # 使用()将原来的list变成了生成器
print(s)  # 打印结果显示s是一个生成器对象
for x in s:
    print(x)


# 定义生成器的另一种方式 使用yield 关键字
# 与定义函数的方法类似，不同的地方是多了yield关键字
# 程序遇到yield关键字会停止，返回结果，下次继续从上次停止的地方开始执行
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(10) # 初始化生成器，获得一个生成器实例
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


215