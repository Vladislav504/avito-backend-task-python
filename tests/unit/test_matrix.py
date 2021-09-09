import pytest
from typing import List

from avito_task.models import Matrix


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("+-----+\n|  10 |\n+-----+", [[10]]),
        (
            """
+-----+-----+
|  10 |  20 |
+-----+-----+
|  50 |  60 |
+-----+-----+
""",
            [[10, 20], [50, 60]],
        ),
        (
            """
+-----+-----+-----+-----+
|  10 |  20 |  40 |  60 |
+-----+-----+-----+-----+
|  50 |  60 | 850 | 360 |
+-----+-----+-----+-----+
|  10 | 120 | 910 |  10 |
+-----+-----+-----+-----+
|  50 |  60 |  50 |  60 |
+-----+-----+-----+-----+
""",
            [
                [10, 20, 40, 60],
                [50, 60, 850, 360],
                [10, 120, 910, 10],
                [50, 60, 50, 60],
            ],
        ),
    ],
)
def test_matrix_from_raw(raw: str, expected: List[List[int]]):
    matrix = Matrix.from_raw(raw)
    assert matrix.matrix == expected


@pytest.mark.parametrize(
    "matrix,expected",
    [
        (Matrix([[10, 20], [30, 40]]), [10, 30, 40, 20]),
        (
            Matrix(
                [
                    [10, 20, 30],
                    [30, 40, 100],
                    [60, 30, 20],
                ]
            ),
            [10, 30, 60, 30, 20, 100, 30, 20, 40],
        ),
        (Matrix([[10]]), [10]),
    ],
)
def test_matrix_spiral(matrix: Matrix, expected: List[int]):
    assert matrix.spiral() == expected
