# coding=utf8
__author__ = 'Sam Raker'


from os import environ
import sys
from time import sleep

from twitter import Twitter
from twitter.oauth import OAuth
from twitter.api import TwitterHTTPError

from truisms import gen


def do_auth():
    return Twitter(auth=OAuth(environ.get("ACCESS_TOKEN"),
                              environ.get("ACCESS_SECRET"),
                              environ.get("API_KEY"),
                              environ.get("API_SECRET")))


def tweet():
    t = do_auth()
    g = gen()
    while True:
        try:
            t.statuses.update(status=g.next())
            sleep(1800)
        except StopIteration:
            g = gen()
        except TwitterHTTPError as e:
            sys.stdout.write(e)
if __name__ == "__main__":
    tweet()
