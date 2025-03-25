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
        print("The matrix is: \n", self.adj_mat)
        result = algorithms.mat_to_list(self.adj_mat)
        print("The result is: \n", result)
        self.assertEqual(result, self.adj_list)
        print("\n")

    def test_reachable_0(self):
        print("The adjacency list is: \n", self.adj_list,
                "The start node is 0")
        result = algorithms.reachable(self.adj_list, 0)
        print("The result is: \n", result)
        self.assertEqual(result, {0, 1, 2, 3, 4})
        print("\n")

    def test_reachable_1(self):
        print("The adjacency list is: \n", self.adj_list,
                "The start node is 3")
        result = algorithms.reachable(self.adj_list, 3)
        print("The result is: \n", result)
        self.assertEqual(result, {3, 4})
        print("\n")

    def test_reachable_2(self):
        print("The adjacency list is: \n", self.adj_list,
                "The start node is 5")
        result = algorithms.reachable(self.adj_list, 5)
        print("The result is: \n", result)
        self.assertEqual(result, set())
        print("\n")


if __name__ == '__main__':
    unittest.main()
