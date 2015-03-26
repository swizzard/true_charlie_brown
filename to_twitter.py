# coding=utf8
__author__ = 'Sam Raker'

import logging
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
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logger = logging.getLogger("true_charlie_brown")
    t = do_auth()
    g = gen()
    while True:
        try:
            new_status = g.next()
            t.statuses.update(status=new_status)
            logger.info("posted status: %s", new_status)
        except StopIteration:
            logger.info("generator exhausted, restarting")
            g = gen()
        except TwitterHTTPError as te:
            logger.exception("%s: %s", type(te), te.message)
        except Exception as e:
            logger.exception(e.message)
            raise
        except SystemExit as se:
            logger.exception("caught SystemExit: %s", se.message)
            raise
        finally:
            sleep(1800)
if __name__ == "__main__":
    tweet()
