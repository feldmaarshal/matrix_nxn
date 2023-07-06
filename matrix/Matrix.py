class Matrix:

    def __init__(self, arr: list[list[int]]):
        self._m = len(arr)  # rows
        self._n = len(arr[0])  # columns
        if any(len(arr[i]) != self._m for i in range(self._m)):
            raise ValueError
        self._arr = arr

    def get_matrix(self):
        return self._arr

    def transpose(self) -> list[list[int]]:
        t_m = self._arr
        for i in range(self._m):
            for j in range(self._n):
                t_m[i][j] = self._arr[j][i]
        return t_m

    def diagonal(self, var: bool) -> list[int]:
        ret = []
        if var:
            for i in range(self._m):
                ret += [self._arr[i][i]]
            return ret

        cnt = self._m
        for i in range(self._m):
            cnt -= 1
            ret += [self._arr[i][cnt]]

        return ret

    def __add__(self, other):
        if isinstance(other, int):
            new = Matrix(self._arr)
            for i in range(self._m):
                for j in range(self._n):
                    new._arr[i][j] += other
            return new

        elif isinstance(other, Matrix):
            new = Matrix([[0] * other._m for _ in range(self._n)])
            for i in range(self._m):
                for j in range(self._n):
                    new._arr[i][j] = self._arr[i][j] + other._arr[i][j]
            return new
        elif isinstance(other, list):
            if self._m == len(other) == len(other[0]):
                new = Matrix([[0] * len(other) for _ in range(len(other))])
                for i in range(self._m):
                    for j in range(self._n):
                        new._arr[i][j] = self._arr[i][j] + other[i][j]
                return new
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, int):
            new = Matrix(self._arr)
            for i in range(self._m):
                for j in range(self._n):
                    new._arr[i][j] -= other
            return new

        elif isinstance(other, Matrix):
            new = Matrix([[0] * other._m for _ in range(self._n)])
            for i in range(self._m):
                for j in range(self._n):
                    new._arr[i][j] = self._arr[i][j] - other._arr[i][j]

        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, int):
            new = Matrix(self._arr)
            for i in range(self._m):
                for j in range(self._n):
                    new._arr[i][j] *= other
            return new

        elif isinstance(other, Matrix):
            new = Matrix([[0] * other._m for _ in range(self._n)])
            if self._m == other._n == other._m:
                for i in range(self._m):
                    for j in range(other._n):
                        for k in range(self._n):
                            new._arr[i][j] += self._arr[i][k] * other._arr[k][j]
                return new
            else:
                raise TypeError

    def get_row(self, index):
        return self._arr[index]

    def get_col(self, index):
        return self.transpose()[index]

    def _get_minor(self, row, col):
        minor_data = []
        for i in range(self._m):
            if i == row:
                continue
            minor_row = []
            for j in range(self._m):
                if j == col:
                    continue
                minor_row.append(self._arr[i][j])
            minor_data.append(minor_row)
        return Matrix(minor_data)

    def determinant(self):
        if self._m == 1:
            return self._arr[0][0]

        det = 0
        sign = 1
        for j in range(self._m):
            minor = self._get_minor(0, j)
            det += sign * self._arr[0][j] * minor.determinant()
            sign *= -1

        return det

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self._m == other._m == other._n:
                for i in range(self._m):
                    for j in range(self._n):
                        if self._arr[i][j] != other._arr[i][j]:
                            return False
                return True
            return False
        elif isinstance(other, list):
            for i in range(self._m):
                for j in range(self._n):
                    if self._arr[i][j] != other[i][j]:
                        return False
            return True

    def __str__(self):
        ans = ''
        for i in range(self._m):
            ans += f'{self._arr[i]}\n'
        ans += f'determinant is {self.determinant()}'
        return ans
