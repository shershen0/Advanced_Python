import numpy as np
import os


class MatrixError(Exception):
    def __init__(self, error: str):
        self.str_error = error

    def __str__(self):
        return str(self.str_error)


class Matrix:
    def __init__(self, mat):
        self.mat = mat
        self.n = len(mat)
        self.m = len(mat[0])
        if self.n <= 0:
            raise MatrixError("Size of matrix not valid")
        if max(map(len, mat)) != min(map(len, mat)):
            raise MatrixError("Matrix has different line size")

    def __add__(self, other):
        try:
            if self.n != other.n or self.m != other.m:
                raise MatrixError("Sizes are different")
            mat = [[0 for _ in range(self.n)] for _ in range(self.m)]
            for i in range(self.n):
                for j in range(other.m):
                    mat[i][j] = self.mat[i][j] + other.mat[i][j]
            return Matrix(mat)
        except MatrixError as error:
            print(error)
            return None

    def __mul__(self, other) -> 'Matrix':
        # sizes n 'x' m
        try:
            if self.n != other.m:
                raise MatrixError("Sizes are different")
            mat = [[0 for _ in range(self.n)] for _ in range(other.n)]
            for i in range(self.n):
                for j in range(other.m):
                    for k in range(self.m):
                        mat[i][j] = self.mat[i][k] * other.mat[k][j]
            return Matrix(mat)
        except MatrixError as error:
            print(error)
            return None

    def __matmul__(self, other):
        # sizes n 'x' m
        try:
            if (self.n != other.n or self.m != other.m):
                raise MatrixError("Sizes are different")
            mat = [[0 for _ in range(self.n)] for _ in range(self.m)]
            for i in range(self.n):
                for j in range(other.m):
                    mat[i][j] = self.mat[i][j] * other.mat[j][i]
            return Matrix(mat)
        except MatrixError as error:
            print(error)
            return None

    def __str__(self):
        s = ""
        for row in self.mat:
            s += str(row) + '\n'
        return s

    def __hash__(self):
        # sum of the elements in the matrix

        hash_m = 0
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                hash_m += self.mat[i][j]
        return hash_m


def main():
    np.random.seed(0)
    A = Matrix([[1, 5], [3, 8]])
    B = Matrix([[1, 0], [0, 1]])
    C = Matrix([[9, 4], [2, 2]])
    D = B

    if (str(A @ B) == str(C @ D)):
        print(str(A @ B) + "\n")
        print(str(C @ D) + "\n")
        print("Bad example")

    if not os.path.exists("artifacts/hard"):
        os.makedirs("artifacts/hard")

    with open("./artifacts/hard/AB.txt", 'w') as f:
        f.write(str(A @ B))
        f.close()

    with open("./artifacts/hard/CD.txt", 'w') as f:
        f.write(str(C @ D))
        f.close()

    with open("./artifacts/hard/hash.txt", 'w') as f:
        f.write(str(hash(A @ B)) + "\n")
        f.write(str(hash(C @ D)) + "\n")
        f.close()

    return 0


if __name__ == '__main__':
    main()
