## Запуск теста

Проведене тестов функции fit_transform с помощью pytest

Запуск теста происходит следующими способами

- python -m pytest -v issue_04.py
- запуска теста через IDE PyCharm

## Проводимые тесты

Проводятся следующие тесты:

- базовый тест:

```python
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected     
```

- проверка с вызовом исключения TypeError в случае подачи числа в качестве аргумента

```python
    with pytest.raises(TypeError):
        fit_transform(0)
```

- проверка вызова функции в случае, подается на вход, не список строк, а перечисление строк в виде нескольких аргументов

```python
    actual = fit_transform('Moscow', 'London')
    expected = [
        ('Moscow', [0, 1]),
        ('London', [1, 0]),
    ]
    assert actual == expected

```
    
- проверка вызова функции в случае, когда не указаны аргументы
  
  
```python
    with pytest.raises(TypeError):
        fit_transform()
```


## Result

```python

============================= test session starts =============================
collecting ... collected 4 items

issue_04.py::test_fit_transform_1 PASSED                                 [ 25%]
issue_04.py::test_fit_transform_2 PASSED                                 [ 50%]
issue_04.py::test_fit_transform_3 PASSED                                 [ 75%]
issue_04.py::test_fit_transform_4 PASSED                                 [100%]

============================== 4 passed in 0.03s ==============================

Process finished with exit code 0


```