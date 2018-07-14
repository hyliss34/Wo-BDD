import unittest

class TestMyBDD(unittest.TestCase):

    def test_1(self):
        print("CECI EST UN TEST")
        a = 1-1
        self.assertEqual(0,a)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

if __name__ == '__main__':
    unittest.main()
