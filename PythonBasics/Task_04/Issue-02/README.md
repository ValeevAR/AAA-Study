## Запуск теста

Запуск теста происходит через запуск соответствующей функции test_decode в IDE PyCharm

## Проводимые тесты

Проводятся следующие тесты:

- проверка декодирования строки:

```python
    decode('.--')
```

- проверка декодирования строки:

```python
    decode('... --- ...-')
```

- проверка декодирования строки:

```python
    decode('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.-')
```

## Результаты теста

```python
C:\Users\Anvar\YandexDisk\_Python\AAAStudy\venv\Scripts\python.exe "C:/Program Files/JetBrains/PyCharm Community Edition 2022.2.2/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py" --target issue_02.py::test_decode 
Testing started at 12:06 ...
Launching pytest with arguments issue_02.py::test_decode --no-header --no-summary -q in C:\Users\Anvar\YandexDisk\_Python\AAAStudy\PythonBasics\Task_04\Issue-02

============================= test session starts =============================
collecting ... collected 3 items

issue_02.py::test_decode[.--A] 
issue_02.py::test_decode[... --- ...-SOS] 
issue_02.py::test_decode[-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.-MAI-PYTHON-2019] 

============================== 3 passed in 0.03s ==============================

Process finished with exit code 0
PASSED                                    [ 33%]PASSED                         [ 66%]PASSED [100%]
```