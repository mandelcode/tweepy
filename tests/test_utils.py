from unittest2 import TestCase

from tweepy.utils import *

class TweepyUtilsTests(TestCase):

    def testparse_datetime(self):
        result = parse_datetime("Wed Aug 27 13:08:45 +0000 2008")
        self.assertEqual(datetime(2008, 8, 27, 13, 8, 45), result)

    def testlist_to_csv(self):
        self.assertEqual("1,2,3", list_to_csv([1,2,3]))
        self.assertEqual("bird,tweet,nest,egg",
                         list_to_csv(["bird", "tweet", "nest", "egg"]))

