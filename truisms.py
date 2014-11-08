# coding=utf8
__author__ = 'Sam Raker'

import re

def gen():
    with open("truisms.txt") as f:
        txt = f.read()
        truisms = [x for x in re.split(r'",?', txt) if x] 
    for x in truisms:
        yield "{}, Charlie Brown".format(x.title())
