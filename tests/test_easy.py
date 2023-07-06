from matrix.Matrix import Matrix
import pytest


@pytest.mark.parametrize('arr, expected_result', [([[1, 2], [1, 2]], [[1, 2], [1, 2]]),
                                                  (
                                                  [[1, 2, 3], [1, 2, 4], [4, 5, 6]], [[1, 2, 3], [1, 2, 4], [4, 5, 6]]),
                                                  ([[1]], [[1]])]
                         )
def test_init_values(arr, expected_result):
    a = Matrix(arr)
    assert a.get_matrix() == expected_result


@pytest.mark.parametrize('arr, exception', [([[1, 2], [2]], ValueError),
                                            ([[1, 2, 3], [4, 5, 6, 7]], ValueError),
                                            ([[1, 2], [2]], ValueError)]
                         )
def test_init_errors(arr, exception):
    with pytest.raises(exception):
        a = Matrix(arr)


@pytest.mark.parametrize('arr, b, expected_result', [
                                                     ([[1]], 1, [[2]]),
                                                     ([[2, 3], [3, 5]], 2, [[4, 5], [5, 7]]),
                                                     ([[2, 3], [3, 5]], [[2, 3], [3, 5]], [[4, 6], [6, 10]])
                                                     ]
                         )
def test_add(arr, b, expected_result):
    a = Matrix(arr)
    assert a + b == expected_result


@pytest.mark.parametrize('arr, b, expected_result', [
                                                     ([[1]], [[1]], True),
                                                     ([[1, 2, 3], [1, 2, 5], [4, 5, 7]], [[2]], False),
                                                     ([[1, 2, 3], [1, 2, 5], [4, 5, 7]], Matrix([[2]]), False),
                                                     ([[2, 3], [2, 3]], [[2, 3], [2, 3]], True),
                                                     ([[2, 3], [2, 3]], Matrix([[2, 3], [2, 3]]), True),
                                                     ])
def test_eq(arr, b, expected_result):
    a = Matrix(arr)
    assert a.__eq__(b) == expected_result


@pytest.mark.parametrize('arr, expected_result', [
                                                    ([[1]], 1),
                                                    ([[1, 2], [1, 2]], 0),
                                                    ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 0),
                                                    ([[1, 2, 3], [1, 2, 7], [9, 2, 3]], 64),
                                                    ([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], 0)
                                                    ])
def test_det(arr, expected_result):
    a = Matrix(arr)
    assert a.determinant() == expected_result
