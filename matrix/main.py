import numpy as np

# -----------------------------
# FUNCTION TO GET MATRIX FROM USER
# -----------------------------
def get_matrix(name="Matrix"):
    while True:
        try:
            rows = int(input(f"Enter number of rows for {name}: "))
            cols = int(input(f"Enter number of columns for {name}: "))
            print(f"Enter the elements for {name} row by row, separated by space:")
            matrix = []
            for i in range(rows):
                row = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row) != cols:
                    raise ValueError(f"Expected {cols} elements, got {len(row)}")
                matrix.append(row)
            return np.array(matrix)
        except Exception as e:
            print("Error:", e)
            print("Try again...\n")

# -----------------------------
# MATRIX OPERATIONS FUNCTIONS
# -----------------------------
def add_matrices(A, B):
    return A + B

def subtract_matrices(A, B):
    return A - B

def multiply_matrices(A, B):
    return A @ B

def transpose_matrix(A):
    return A.T

def determinant_matrix(A):
    if A.shape[0] != A.shape[1]:
        raise ValueError("Determinant requires a square matrix")
    return np.linalg.det(A)

# -----------------------------
# INTERACTIVE MENU
# -----------------------------
def main():
    print("===== MATRIX OPERATIONS TOOL =====")
    while True:
        print("\nSelect an operation:")
        print("1. Addition (A + B)")
        print("2. Subtraction (A - B)")
        print("3. Multiplication (A x B)")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            A = get_matrix("Matrix A")
            B = get_matrix("Matrix B")
            if A.shape != B.shape:
                print("Error: Matrices must have the same dimensions for addition.")
                continue
            print("Result of A + B:\n", add_matrices(A, B))

        elif choice == "2":
            A = get_matrix("Matrix A")
            B = get_matrix("Matrix B")
            if A.shape != B.shape:
                print("Error: Matrices must have the same dimensions for subtraction.")
                continue
            print("Result of A - B:\n", subtract_matrices(A, B))

        elif choice == "3":
            A = get_matrix("Matrix A")
            B = get_matrix("Matrix B")
            if A.shape[1] != B.shape[0]:
                print("Error: Number of columns in A must equal number of rows in B for multiplication.")
                continue
            print("Result of A x B:\n", multiply_matrices(A, B))

        elif choice == "4":
            A = get_matrix("Matrix")
            print("Transpose of the matrix:\n", transpose_matrix(A))

        elif choice == "5":
            A = get_matrix("Matrix")
            try:
                det = determinant_matrix(A)
                print(f"Determinant of the matrix: {det}")
            except ValueError as e:
                print("Error:", e)

        elif choice == "6":
            print("Exiting Matrix Operations Tool. Goodbye!")
            break

        else:
            print("Invalid choice! Enter a number between 1-6.")

if __name__ == "__main__":
    main()