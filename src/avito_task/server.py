import aiohttp
from aiohttp.client_reqrep import ClientResponse

from avito_task.exceptions import ServerError


async def handle_response(response: ClientResponse) -> str:
    """
    Обрабатывает ответ сервера.
    При возникновении ошибки 5xx кидает ServerError.
    """
    if response.status >= 500:
        raise ServerError(response.reason)
    return await response.text()


async def get_raw_matrix(url: str) -> str:
    """Получет матрицу по url."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await handle_response(response)
