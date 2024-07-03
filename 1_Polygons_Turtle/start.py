#! /usr/bin/python3

#
# Use tortle module to draw
#

from turtle import *
import time

def star(side):
    for i in range(5):
        forward(side)
        right(145)

shape('turtle')
speed(0)
side = 5
for i in range(60):
    star(side)
    side += 10
time.sleep(1000)
