import numpy as np
import os


class StrMixin:
    def __str__(self):
        s = ""
        for row in self.mat:
            s += str(row) + '\n'
        return s


class WriteToFileMixin:
    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))


class SetterGetterMixin:
    def __get__(self):
        return self.mat

    def __set__(self, new_mat):
        self.mat = new_mat


class MatrixMixin(np.lib.mixins.NDArrayOperatorsMixin, SetterGetterMixin, WriteToFileMixin, StrMixin):
    def __init__(self, mat):
        self.mat = np.asarray(mat)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())

        inputs = tuple(x.mat if isinstance(x, MatrixMixin) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, MatrixMixin) else x
                for x in out)

        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)


def main():
    np.random.seed(0)
    A = MatrixMixin(np.random.randint(0, 10, (10, 10)))
    B = MatrixMixin(np.random.randint(0, 10, (10, 10)))

    if not os.path.exists("artifacts/medium"):
        os.makedirs("artifacts/medium")

    with open("./artifacts/medium/matrix+.txt", 'w') as f:
        f.write(str(A + B))

    with open("./artifacts/medium/matrix*.txt", 'w') as f:
        f.write(str(A * B))

    with open("./artifacts/medium/matrix@.txt", 'w') as f:
        f.write(str(A @ B))

    f.close()
    return 0


if __name__ == '__main__':
    main()
