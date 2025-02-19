import os
from sparse_matrix import SparseMatrix
from operations import add_matrices, subtract_matrices, multiply_matrices

def main():
    print("Sparse Matrix Operations")
    
    # Get input file paths from user
    file1 = input("Enter path for first matrix file: ").strip()
    file2 = input("Enter path for second matrix file: ").strip()

    # Load matrices
    mat1 = SparseMatrix(file1)
    mat2 = SparseMatrix(file2)

    # Choose operation
    print("\nChoose operation:\n1. Addition\n2. Subtraction\n3. Multiplication")
    choice = input("Enter your choice (1/2/3): ").strip()

    result = None  # Store the result matrix

    if choice == '1':
        result = add_matrices(mat1, mat2)
    elif choice == '2':
        result = subtract_matrices(mat1, mat2)
    elif choice == '3':
        result = multiply_matrices(mat1, mat2)
    else:
        print("❌ Invalid choice!")
        return
    
    # If operation was successful, save the result
    if result:
        output_file = input("Enter output file name (default: result_matrix.txt): ").strip()
        if not output_file:
            output_file = "result_matrix.txt"  # Default output file
        result.save_to_file(output_file)

if __name__ == "__main__":
    main()