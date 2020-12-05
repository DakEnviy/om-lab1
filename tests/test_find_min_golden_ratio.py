import unittest
from tests.defaults_functions import epsilon, places, test_functions
from algo.find_min_golden_ratio import find_min_golden_ratio


class TestFindMinGoldenRatio(unittest.TestCase):
    def test_func1(self):
        func, a, b, result = test_functions[0]
        self.assertAlmostEqual(find_min_golden_ratio(func, a, b, epsilon=epsilon), result, places=places)

    def test_func2(self):
        func, a, b, result = test_functions[1]
        self.assertAlmostEqual(find_min_golden_ratio(func, a, b, epsilon=epsilon), result, places=places)

    def test_func3(self):
        func, a, b, result = test_functions[2]
        self.assertAlmostEqual(find_min_golden_ratio(func, a, b, epsilon=epsilon), result, places=places)

    def test_func4(self):
        func, a, b, result = test_functions[3]
        self.assertAlmostEqual(find_min_golden_ratio(func, a, b, epsilon=epsilon), result, places=places)

    def test_func5(self):
        func, a, b, result = test_functions[4]
        self.assertAlmostEqual(find_min_golden_ratio(func, a, b, epsilon=epsilon), result, places=places)


if __name__ == '__main__':
    unittest.main()
