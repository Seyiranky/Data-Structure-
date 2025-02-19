# sparse_matrix.py
class SparseMatrix:
    def __init__(self, file_path=None, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.data = {}  # Store values as {(row, col): value}
        
        if file_path:
            self._load_from_file(file_path)
    
    def _load_from_file(self, file_path):
        """Reads the sparse matrix from the file and stores it in dictionary form."""
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                self.rows = int(lines[0].split('=')[1].strip())
                self.cols = int(lines[1].split('=')[1].strip())
                
                for line in lines[2:]:
                    line = line.strip()
                    if not line:
                        continue  # Ignore empty lines
                    
                    if not (line.startswith("(") and line.endswith(")")):
                        raise ValueError("Input file has wrong format")
                    
                    elements = line[1:-1].split(",")
                    if len(elements) != 3:
                        raise ValueError("Input file has wrong format")
                    
                    try:
                        row, col, value = map(int, [elem.strip() for elem in elements])
                    except ValueError:
                        raise ValueError("Input file has wrong format")
                    
                    self.set_element(row, col, value)
                    
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File {file_path} not found.")
    
    def get_element(self, row, col):
        """Returns the value at the specified position or zero if not present."""
        return self.data.get((row, col), 0)
    
    def set_element(self, row, col, value):
        """Sets a value in the sparse matrix."""
        if value == 0:
            self.data.pop((row, col), None)  # Remove entry if value is zero
        else:
            self.data[(row, col)] = value
    
    def display(self):
        """Displays non-zero elements of the sparse matrix."""
        print(f"SparseMatrix({self.rows}x{self.cols}) with {len(self.data)} non-zero elements")
        for (row, col), value in sorted(self.data.items()):
            print(f"({row}, {col}): {value}")
    
    def save_to_file(self, filename):
        """Writes the sparse matrix to a file in the required format."""
        with open(filename, 'w') as f:
            f.write(f"rows={self.rows}\n")
            f.write(f"cols={self.cols}\n")
            for (row, col), value in sorted(self.data.items()):
                f.write(f"({row}, {col}, {value})\n")

# operations.py
def add_matrices(mat1, mat2):
    max_rows = max(mat1.rows, mat2.rows)
    max_cols = max(mat1.cols, mat2.cols)
    
    result = SparseMatrix(rows=max_rows, cols=max_cols)
    
    # Add elements from mat1
    for (row, col), value in mat1.data.items():
        result.set_element(row, col, value + mat2.get_element(row, col))
    
    # Add elements from mat2 (if they weren't already in mat1)
    for (row, col), value in mat2.data.items():
        if (row, col) not in mat1.data:
            result.set_element(row, col, value)
    
    return result

def subtract_matrices(mat1, mat2):
    max_rows = max(mat1.rows, mat2.rows)
    max_cols = max(mat1.cols, mat2.cols)
    
    result = SparseMatrix(rows=max_rows, cols=max_cols)
    
    # Subtract elements from mat1
    for (row, col), value in mat1.data.items():
        result.set_element(row, col, value - mat2.get_element(row, col))
    
    # Handle elements that are only in mat2
    for (row, col), value in mat2.data.items():
        if (row, col) not in mat1.data:
            result.set_element(row, col, -value)
    
    return result

def multiply_matrices(mat1, mat2):
    if mat1.cols != mat2.rows:
        raise ValueError("Matrix multiplication is not possible: Column count of first matrix must equal row count of second matrix")
    
    result = SparseMatrix(rows=mat1.rows, cols=mat2.cols)
    
    for (row1, col1), value1 in mat1.data.items():
        for (row2, col2), value2 in mat2.data.items():
            if col1 == row2:
                current = result.get_element(row1, col2)
                result.set_element(row1, col2, current + value1 * value2)
    
    return result

# test_sparse_matrix.py
import unittest

class TestSparseMatrix(unittest.TestCase):
    def setUp(self):
        self.m1 = SparseMatrix(rows=3, cols=3)
        self.m1.set_element(0, 1, 5)
        self.m1.set_element(1, 2, 10)
        
        self.m2 = SparseMatrix(rows=3, cols=3)
        self.m2.set_element(0, 1, 2)
        self.m2.set_element(1, 2, 8)
    
    def test_addition(self):
        result = add_matrices(self.m1, self.m2)
        self.assertEqual(result.get_element(0, 1), 7)
        self.assertEqual(result.get_element(1, 2), 18)
    
    def test_subtraction(self):
        result = subtract_matrices(self.m1, self.m2)
        self.assertEqual(result.get_element(0, 1), 3)
        self.assertEqual(result.get_element(1, 2), 2)
    
    def test_multiplication(self):
        result = multiply_matrices(self.m1, self.m2)
        self.assertEqual(result.get_element(0, 1), 0)  # No overlapping elements
        self.assertEqual(result.get_element(1, 2), 0)  # No overlapping elements

if __name__ == '__main__':
    unittest.main()