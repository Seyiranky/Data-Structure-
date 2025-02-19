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
                        row, col, value = int(elements[0]), int(elements[1]), int(elements[2])
                    except ValueError:
                        raise ValueError("Input file has wrong format")

                    self.set_element(row, col, value)

        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")

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
        for (row, col), value in self.data.items():
            print(f"({row}, {col}): {value}")

    def save_to_file(self, filename):
        """Writes the sparse matrix to a file in the required format."""
        with open(filename, 'w') as f:
            f.write(f"rows={self.rows}\n")
            f.write(f"cols={self.cols}\n")
            for (row, col), value in self.data.items():
                f.write(f"({row}, {col}, {value})\n")
        print(f"✅ Output saved to {filename}")