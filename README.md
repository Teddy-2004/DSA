# Sparse Matrix Operations

This project implements a custom sparse matrix class in Python that supports reading from file and performing addition, subtraction, and multiplication. It is designed to work without using any standard libraries like `regex`, `collections`, or other helpers beyond basic Python.

## 📁 Directory Structure

```
/dsa/sparse_matrix/code/src/          # Python code lives here
/dsa/sparse_matrix/sample_inputs/     # Sample input matrix files
```

## 📜 File Format

Each matrix file should be in this format:

```
rows=number of rows
cols=number of column
(row_index, column_index, value)
(row_index, column_index, value)
...
```

* Only non-zero elements are listed.
* All unspecified values are assumed to be zero.

## 🚀 Features

* Efficient storage using dictionary to store non-zero values
* Supports:

  * Matrix Addition
  * Matrix Subtraction
  * Matrix Multiplication
* Input validation and exception handling
* Outputs result to console and optionally to a `result.txt` file

## 🧪 Usage

Run the main script:

```bash
python3 sparse_matrix.py
```

Follow the prompt to choose one of the following operations:

* `add`
* `subtract`
* `multiply`

## 📌 Important Constraints

* For **addition and subtraction**, both matrices must have the same dimensions.
* For **multiplication**, the number of columns in Matrix A must match the number of rows in Matrix B.

## ⚠️ Error Handling

* Throws `ValueError` for incompatible operations.
* Validates formatting of input files and halts if structure is invalid.

## 🛠️ Customization

You can modify the paths to input files in the main block:

```python
path1 = "../../sample_inputs/easy_sample_03_1.txt"
path2 = "../../sample_inputs/easy_sample_03_2.txt"
```
This samples can only be added and subtracted, but not multiplyed as the number of rows and columns do not allow multiplication. If you want to test multiplication, change the path to other samples in sample directory, like **easy_sample_01_2.txt** and **easy_sample_01_03.txt**.

## ✅ Requirements Fulfilled

* No use of built-in libraries like regex, collections, etc.
* Clear separation of code and input files
* Fully documented source code with internal comments
* Follows matrix rules and applies exception handling accordingly

  **Tedla Tesfaye Godebo**
