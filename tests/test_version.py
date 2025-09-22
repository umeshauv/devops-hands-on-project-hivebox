import unittest
from version import get_version

class TestStringMethods(unittest.TestCase):

    def test_version(self):
        self.assertEqual(get_version(), 'v0.0.1')

if __name__ == '__main__':
    unittest.main()