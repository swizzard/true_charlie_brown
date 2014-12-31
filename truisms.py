# coding=utf8
__author__ = 'Sam Raker'


def gen():
    with open("truisms.txt") as f:
        i = iter(f.readlines())
    while True:
        try:
            yield "{}, Charlie Brown".format(i.next().rstrip().title())
        except StopIteration:
            break
