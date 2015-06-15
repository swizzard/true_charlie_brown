# coding=utf8
__author__ = 'Sam Raker'

from twitter.oauth import OAuth

from botmaster import gen_tweet
from miniconfig import config

@gen_tweet(auth=OAuth(**config), interval=1800)
def gen():
    with open("truisms.txt") as f:
        i = iter(f.readlines())
    while True:
        try:
            yield "{}, Charlie Brown".format(i.next().rstrip().title())
        except StopIteration:
            break


if __name__ == "__main__":
    gen()
