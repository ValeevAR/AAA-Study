## Command

Запуск теста происходит следующими способами

- python -m unittest -v issue_05.py
- запуска теста через IDE PyCharm

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