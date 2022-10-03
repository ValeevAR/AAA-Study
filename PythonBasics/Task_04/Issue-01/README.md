## Запуск теста

Запус теста выполняется одним из способов ниже:

- Ввод в командную строку:
```python
python -m doctest -o NORMALIZE_WHITESPACE -v issue-01.py
```
- Запуск теста через IDE PyCharm

## Проводимые тесты

Проводятся следующие тесты:

- проверка кодирования строки: 
```python
    encode('A')
```
- проверка кодирования строки:
```python
    encode('MAI-PYTHON-2019')
```

- проверка кодирования строки:
```python
    encode('SOS')
```

- выполнения теста в включенных флагом NORMALIZE_WHITESPACE:
```python
    encode('TEST WITH NORMALIZE WHITESPACE')
```

- выполнения теста с пропуском аргумента в функции, проверка вызова TypeError
```python
    encode()
```

- выполнения теста с неверным типом аргумента в функции, проверка вызова TypeError
```python
    encode(123)
```

## Результаты теста


```python
Trying:
    encode('A')
Expecting:
    '.-'
ok
Trying:
    encode('MAI-PYTHON-2019')
Expecting:
    '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'
ok
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('TEST WITH NORMALIZE WHITESPACE')
Expecting:
        '- . ... -   .-- .. - ....   -. --- .-. -- .- .-.. .. --.. .   .-- .... .. - . ... .--. .- -.-. .'
ok
Trying:
    encode()
Expecting:
    Traceback (most recent call last):
    ...
    TypeError: encode() missing 1 required positional argument: 'message'
ok
Trying:
    encode(123)
Expecting:
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not iterable
ok
2 items had no tests:
    issue-01
    issue-01.decode
1 items passed all tests:
   6 tests in issue-01.encode
6 tests in 3 items.
6 passed and 0 failed.
Test passed.
(venv) PS C:\Users\Anvar\YandexDisk\_Python\AAAStudy\PythonBasics\Task_04\Issue-01>

```


