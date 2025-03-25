import unittest
import algorithms

class Test(unittest.TestCase):
    adj_mat = [[0, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0]]

    adj_list = [[1, 3], [2], [0], [4], [3], []]

    def test_mat_to_list_0(self):
        result = algorithms.mat_to_list(self.adj_mat)
        self.assertEqual(result, self.adj_list)

    def test_reachable_0(self):
        result = algorithms.reachable(self.adj_list, 0)
        self.assertEqual(result, {0, 1, 2, 3, 4})

    def test_reachable_1(self):

        result = algorithms.reachable(self.adj_list, 3)
        self.assertEqual(result, {3, 4})

    def test_reachable_2(self):
        result = algorithms.reachable(self.adj_list, 5)
        self.assertEqual(result, set())


if __name__ == '__main__':
    unittest.main()
