## Command

Запуск теста происходит следующими способами

- python -m unittest -v issue_03.py
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
    self.assertEqual(actual, expected)        
```

- проверка с использованием assertNotIn о не включении элемента в результат :

```python
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        not_in = 'Moon'
        self.assertNotIn(not_in, actual)
```

- проверка с вызовом исключения TypeError в случае подачи числа в качестве аргумента

```python
        with self.assertRaises(TypeError):
            fit_transform(0)
```

- проверка вызова функции в случае, подается на вход, не список строк, а перечисление строк в виде нескольких аргументов

```python
    actual = fit_transform('Moscow', 'London')
    expected = [
        ('Moscow', [0, 1]),
        ('London', [1, 0]),
    ]
    self.assertEqual(actual, expected)
```
    
- проверка вызова функции в случае, когда не указаны аргументы
  
  
```python
    def test_fit_transform_5(self):
        with self.assertRaises(TypeError):
            fit_transform()
```


## Result

```python

issue_03.py::TestFitTransform::test_fit_transform_1 PASSED               [ 20%]
issue_03.py::TestFitTransform::test_fit_transform_2 PASSED               [ 40%]
issue_03.py::TestFitTransform::test_fit_transform_3 PASSED               [ 60%]
issue_03.py::TestFitTransform::test_fit_transform_4 PASSED               [ 80%]
issue_03.py::TestFitTransform::test_fit_transform_5 PASSED               [100%]

============================== 5 passed in 0.03s ==============================

Process finished with exit code 0

```