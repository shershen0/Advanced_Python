import numpy as np
import os


class MatrixError(Exception):
    def __init__(self, error: str):
        self.str_error = error

    def __str__(self):
        return str(self.str_error)


class Matrix:
    def __init__(self, mat: list):
        self.mat = mat
        self.n = len(mat)
        self.m = len(mat[0])
        if (self.n <= 0):
            raise MatrixError("Size of matrix not valid")
        if (max(map(len, mat)) != min(map(len, mat))):
            raise MatrixError("Matrix has different line size")

    def __add__(self, other: list):
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

    def __mul__(self, other: list) -> 'Matrix':
        # sizes n 'x' m
        try:
            if (self.n != other.m):
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

    def __matmul__(self, other: list):
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


def main():
    np.random.seed(0)
    A = Matrix(np.random.randint(0, 10, (10, 10)))
    B = Matrix(np.random.randint(0, 10, (10, 10)))

    if not os.path.exists("artifacts/easy"):
        os.makedirs("artifacts/easy")

    with open("./artifacts/easy/matrix+.txt", 'w') as f:
        f.write(str(A + B))
        f.close()

    with open("./artifacts/easy/matrix*.txt", 'w') as f:
        f.write(str(A * B))
        f.close()

    with open("./artifacts/easy/matrix@.txt", 'w') as f:
        f.write(str(A @ B))
        f.close()

    return 0


if __name__ == '__main__':
    main()
