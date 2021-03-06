# Тестовое Backend задание для стажировки в Avito
Задание представляло собой написание библиотеки на Python,
в которой надо было реализовать функцию получения квадтратичной матрицы
в виде обхода по спирали. Размерность квадратичной матрицы не имеет значения.

В функцию передается url, откуда 
и берется матрица в текстовом виде. 

Взаимодействие с сервером
внутри библиотеки реализованно асинхронно посредством aiohttp.

# Установка

Скопировать репозиторий:
```bash
git clone https://github.com/Vladislav504/avito-backend-task-python.git avito_task
cd avito_task
```
Установить библиотеку:
```bash
pip install .
```

Использовать в своем коде:
```python
from avito_task import get_matrix

spiral = await get_matrix('some_url')
```

# Обработка ошибок
При возникновении ошибки со стороны сервера или сети, выдается исключение `ServerError`. Чтобы увидеть причину ошибки, нужно передать объект исключения методу `str` в python.
```python
try:
    # something went wrong
    get_matrix('some_url')
except ServerError as e:
    reason = str(e)
    # display error message
    print(reason)
```

