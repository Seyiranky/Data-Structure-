from sparse_matrix import SparseMatrix  #Import the SparseMatrix class
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

    result = SparseMatrix(rows=mat1.rows, cols=mat1.cols)
    
    for (row, col), value in mat1.data.items():
        result.set_element(row, col, value - mat2.get_element(row, col))

    for (row, col), value in mat2.data.items():
        if (row, col) not in mat1.data:
            result.set_element(row, col, -value)

    return result

def multiply_matrices(mat1, mat2):
    if mat1.cols != mat2.rows:
        raise ValueError("Matrix multiplication is not possible: Column count of first matrix must equal row count of second matrix")

    result = SparseMatrix(rows=mat1.rows, cols=mat2.cols)

    for (row, col1), value1 in mat1.data.items():
        for col2 in range(mat2.cols):
            value2 = mat2.get_element(col1, col2)
            if value2 != 0:
                result.set_element(row, col2, result.get_element(row, col2) + value1 * value2)

    return result
