import unittest
from sparse_matrix import SparseMatrix
from operations import add_matrices, subtract_matrices, multiply_matrices

class TestSparseMatrix(unittest.TestCase):
    def setUp(self):
        self.m1 = SparseMatrix(num_rows=3, num_cols=3)
        self.m1.setElement(0, 1, 5)
        self.m1.setElement(1, 2, 10)
        self.m2 = SparseMatrix(num_rows=3, num_cols=3)
        self.m2.setElement(0, 1, 2)
        self.m2.setElement(1, 2, 8)

    def test_addition(self):
        result = add_matrices(self.m1, self.m2)
        self.assertEqual(result.getElement(0, 1), 7)
        self.assertEqual(result.getElement(1, 2), 18)

    def test_subtraction(self):
        result = subtract_matrices(self.m1, self.m2)
        self.assertEqual(result.getElement(0, 1), 3)
        self.assertEqual(result.getElement(1, 2), 2)

if __name__ == '__main__':
    unittest.main()