#! /usr/bin/python3

#
# Use tortle module to draw
#

from turtle import *
import time

def square():
    for i in range(4):
        forward(start)
        right(90)

shape('turtle')
speed(0)

time.sleep(1)
start = 5
for i in range(72):
    square()
    right(5)
    start += 10

time.sleep(1000)
