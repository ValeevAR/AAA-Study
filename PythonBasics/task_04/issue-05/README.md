## Запуск теста

Запуск теста функции what_is_year_now происходит следующими способами

- python -m unittest -v issue_05.py
- запуска теста через IDE PyCharm

## Проводимые тесты

Для проведения теста вместо urllib.request.urlopen используется nittest.mock для замены реального обращения к API.
Подставляются данные из файлов test1.json ... test4.json

Проводятся следующие тест:

- Тест выполнения формата YYYY-MM-DD

  Исходные данные для теста

```python
    {
        "$id": "1",
        "currentDateTime": "2022-10-02T18:55Z",
        "utcOffset": "00:00:00",
        "isDayLightSavingsTime": false,
        "dayOfTheWeek": "Sunday",
        "timeZoneName": "UTC",
        "currentFileTime": 133092105284286200,
        "ordinalDate": "2022-275",
        "serviceResponse": null
    }
```

код для теста

```python
    with open("test1.json", "r") as test_data:
        with patch("urllib.request.urlopen") as mocked_get_cases:
            mocked_get_cases.return_value = test_data
            self.assertEqual(what_is_year_now(), 2022)
```

- Тест выполнения формата DD.MM.YYYY

  Исходные данные для теста

```python
    {
        "$id": "1",
        "currentDateTime": "01.03.2019"
    }
```

код для теста

```python
    with open("test2.json", "r") as test_data:
        with patch("urllib.request.urlopen") as mocked_get_cases:
            mocked_get_cases.return_value = test_data
            self.assertEqual(what_is_year_now(), 2019)
```

- Тест выполнения неверного формата DD.MM.YYYY

Исходные данные для теста

```python
    {
        "$id": "1",
        "currentDateTime": "первое января 2022"
    }
```

код для теста

```python
    with open("test3.json", "r") as test_data:
        with patch("urllib.request.urlopen") as mocked_get_cases:
            mocked_get_cases.return_value = test_data
            with self.assertRaises(ValueError):
                what_is_year_now()
```

- Тест на наличие ключа currentDateTime

Исходные данные для теста

```python
    {
        "$id": "1",
        "WrongAttribute": "2022-10-02T18:55Z"
    }
```

код для теста

```python
    with open("test4.json", "r") as test_data:
        with patch("urllib.request.urlopen") as mocked_get_cases:
            mocked_get_cases.return_value = test_data
            with self.assertRaises(KeyError):
                what_is_year_now()
```

## Result

```python
test_what_is_year_now_1 (issue_05.TestFitTransform)
Тест выполнения формата YYYY-MM-DD ... ok
test_what_is_year_now_2 (issue_05.TestFitTransform)
Тест выполнения формата DD.MM.YYYY ... ok
test_what_is_year_now_3 (issue_05.TestFitTransform)
Тест выполнения неверного формата DD.MM.YYYY ... ok
test_what_is_year_now_4 (issue_05.TestFitTransform)
Тест на наличие ключа currentDateTime ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK
```

## Анализ покрытия кода

Анализ покрытия кода выполняется последовательным запуском команд

```python
coverage run -m unittest issue_05.py
coverage report
coverage html
```

Результ сохранен в файл issue_05_py.html

В результате тестирование был покрыт весь код анализируемой функции
