# Algorithm to calculate matrixs
class SparseMatrix:
    def __init__(self, file_path=None, num_rows=0, num_cols=0):
        # Dictionary to store elements with row and col as keys
        self.rows = num_rows
        self.cols = num_cols
        self.elements = {}

        # Get matrix file from a file path provided
        if file_path:
            self.load_from_file(file_path)

    def load_from_file(self, path):
        with open(path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            # Remove empty lines and strip whitespace
            line = line.strip()
            if not line:
                continue
            if line.startswith("rows="):
                 # Parse the first two lines to get matrix dimensions
                self.rows = int(line.split("=")[1])
            elif line.startswith("cols="):
                self.cols = int(line.split("=")[1])
                # Parse each element line
            elif line.startswith("(") and line.endswith(")"):
                content = line[1:-1]
                parts = content.split(",")
                if len(parts) != 3:
                    raise ValueError("Input file has wrong format")
                try:
                    r = int(parts[0].strip())
                    c = int(parts[1].strip())
                    v = int(parts[2].strip())
                except:
                    raise ValueError("Input file has wrong format")
                self.set_element(r, c, v)
            else:
                raise ValueError("Input file has wrong format")

    def set_element(self, row, col, value):
        if value != 0:
            self.elements[(row, col)] = value
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def get_element(self, row, col):
        return self.elements.get((row, col), 0)

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition.")
        result = SparseMatrix(num_rows=self.rows, num_cols=self.cols)
        for key in set(self.elements.keys()).union(other.elements.keys()):
            result.set_element(key[0], key[1],
                               self.get_element(*key) + other.get_element(*key))
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for subtraction.")
        result = SparseMatrix(num_rows=self.rows, num_cols=self.cols)
        for key in set(self.elements.keys()).union(other.elements.keys()):
            result.set_element(key[0], key[1],
                               self.get_element(*key) - other.get_element(*key))
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication.")
        result = SparseMatrix(num_rows=self.rows, num_cols=other.cols)
        # Multiply only non-zero values
        for (r1, c1), v1 in self.elements.items():
            for c2 in range(other.cols):
                v2 = other.get_element(c1, c2)
                if v2 != 0:
                    prev = result.get_element(r1, c2)
                    result.set_element(r1, c2, prev + v1 * v2)
        return result

    def print(self):
        print(f"rows={self.rows}")
        print(f"cols={self.cols}")
        for (r, c), v in sorted(self.elements.items()):
            print(f"({r}, {c}, {v})")

# Main execution block
if __name__ == "__main__":
    path1 = "../../sample_inputs/easy_sample_01_2.txt"
    path2 = "../../sample_inputs/easy_sample_01_03.txt"

    m1 = SparseMatrix(file_path=path1)
    m2 = SparseMatrix(file_path=path2)

    try:
        op = input("Choose operation (add / subtract / multiply): ").strip().lower()
        if op == "add":
            result = m1.add(m2)
        elif op == "subtract":
            result = m1.subtract(m2)
        elif op == "multiply":
            result = m1.multiply(m2)
        else:
            print("Invalid operation")
            exit()
    except ValueError as e:
        print(f"Error: {e}")
        exit()


    print("\nResult:")
    result.print()

