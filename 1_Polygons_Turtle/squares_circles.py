#! /usr/bin/python3

#
# Use tortle module to draw
#

from turtle import *
import time

def square():
    for i in range(4):
        forward(100)
        right(90)

shape('turtle')
speed(0)

time.sleep(1)
for i in range(72):
    square()
    right(5)
time.sleep(1000)
