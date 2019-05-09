import unittest

from App import hello


class MyFirstTest(unittest.TestCase):

    def test_Hello(self):
        self.assertEqual(hello(),'Hello World!')


if __name__ == '__main__':
   unittest.main()8