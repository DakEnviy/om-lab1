import unittest
from tests.defaults_functions import epsilon, places, test_functions_multi
from algo.find_min_golden_ratio import find_min_golden_ratio
from algo.find_min_brent import find_min_brent


class TestMultimodalFunction(unittest.TestCase):
    def test_golden_ratio_func1(self):
        func, a, b, result = test_functions_multi[0]
        self.assertAlmostEqual(find_min_golden_ratio(func, a, b, epsilon=epsilon), result, places=places)

    def test_brent_func1(self):
        func, a, b, result = test_functions_multi[0]
        self.assertAlmostEqual(find_min_brent(func, a, b, epsilon=epsilon), result, places=places)


if __name__ == '__main__':
    unittest.main()
