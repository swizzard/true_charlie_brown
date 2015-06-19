# coding=utf8
__author__ = 'Sam Raker'

from botmaster import _auth, gen_tweet
from miniconfig import config

@gen_tweet(auth=_auth(**config), interval=1800, ignore=[187], restart=True)
def gen():
    with open("truisms.txt") as f:
        for line in f:
            yield "{}, Charlie Brown".format(line.title().rstrip())


if __name__ == "__main__":
    gen()
