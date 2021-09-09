from typing import List

from avito_task.utils import numbers_filter, spiral_algorithm


class Matrix:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix

    def spiral(self) -> List[int]:
        return spiral_algorithm(self.matrix)

    @classmethod
    def from_raw(cls, raw: str):
        """
        Трансформирует полученную с сервера матрицу в
        обычную матрицу целых чисел.
        """
        lines = raw.split("\n")
        matrix = numbers_filter(lines)
        return cls(matrix)
