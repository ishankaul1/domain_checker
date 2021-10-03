import unittest
from edit_distance import editDist_DP

class TestEditDist(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(editDist_DP('cat', 'fat'), 1)
        self.assertEqual(editDist_DP('ppp', 'ppc'), 1)

    def test_difflengths_simple(self):
        self.assertEqual(editDist_DP('xxx', 'xxxxxxx'), 4)
        self.assertEqual(editDist_DP('xxxxxxxxxx', 'xxx'), 7)

    def test_complex(self):
        self.assertEqual(editDist_DP('54321', 'xxx'), 5)
        self.assertEqual(editDist_DP('123x5', 'ppx'), 4)
        self.assertEqual(editDist_DP("zoologicoarchaeologist", "zoogeologist"), 10)

if __name__ == '__main__':
    unittest.main()