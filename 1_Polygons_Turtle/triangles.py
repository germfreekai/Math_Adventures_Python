#! /usr/bin/python3

#
# Use tortle module to draw
#

from turtle import *
import time

def triangle(side):
    right(60)
    for i in range(3):
        forward(side)
        right(120)

shape('turtle')
triangle(100)
time.sleep(1000)
