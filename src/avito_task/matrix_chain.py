from typing import List

from avito_task.server import get_raw_matrix
from avito_task.models import Matrix


async def get_matrix(url: str) -> List[int]:
    """Обходит матрицу, полученную по url, по спирали"""
    raw_matrix = await get_raw_matrix(url)
    matrix = Matrix.from_raw(raw_matrix)
    return matrix.spiral()
