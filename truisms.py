# coding=utf8
__author__ = 'Sam Raker'

from twitter.oauth import OAuth

from botmaster import gen_tweet
from miniconfig import config

@gen_tweet(auth=OAuth(**config), interval=1800, ignore=[187], restart=True)
def gen():
    with open("truisms.txt") as f:
        i = iter(f.readlines())
    while True:
        yield "{}, Charlie Brown".format(i.next().title().rstrip())


if __name__ == "__main__":
    gen()
