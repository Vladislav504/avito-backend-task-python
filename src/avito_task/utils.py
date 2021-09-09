from typing import List


def numbers_filter(lines: List[str]) -> List[List[int]]:
    """Превращает строки с числами и перегородками в матрицу чисел."""
    result = filter(lambda x: x.startswith("|"), lines)
    result = map(lambda x: x.split("|"), result)
    result = [filter(lambda x: len(x) > 0, row) for row in result]
    result = [list(map(lambda x: int(x.strip()), row)) for row in result]
    return result


def spiral_algorithm(matrix: List[List[int]]):
    """Алгоритм обхода матрицы по спирали против часовой стрелки."""
    columns = rows = len(matrix)
    columns_step = [0, 1, 0, -1]
    rows_step = [1, 0, -1, 0]
    step_type = 0
    current_row = 0
    current_column = 0
    visited = [[False for _ in range(columns)] for _ in range(rows)]

    result = []
    for _ in range(columns * rows):
        visited[current_row][current_column] = True
        result.append(matrix[current_row][current_column])
        current_column += columns_step[step_type]
        current_row += rows_step[step_type]
        if not (
            (current_column >= 0 and current_column < columns)
            and (current_row >= 0 and current_row < rows)
            and (not visited[current_row][current_column])
        ):
            current_column -= columns_step[step_type]
            current_row -= rows_step[step_type]
            step_type = (step_type + 1) % 4
            current_column += columns_step[step_type]
            current_row += rows_step[step_type]
    return result
