import urllib.request
import json
import unittest
from unittest.mock import patch

API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


class TestFitTransform(unittest.TestCase):
    # Класс для проведения теста. Вместо urllib.request.urlopen используются данные из файлов

    def test_what_is_year_now_1(self):
        '''
        Тест выполнения формата YYYY-MM-DD

        Исходные данные для теста

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
        '''

        with open("test1.json", "r") as test_data:
            with patch("urllib.request.urlopen") as mocked_get_cases:
                mocked_get_cases.return_value = test_data
                self.assertEqual(what_is_year_now(), 2022)

    def test_what_is_year_now_2(self):
        '''
        Тест выполнения формата DD.MM.YYYY

        Исходные данные для теста

        {
            "$id": "1",
            "currentDateTime": "01.03.2019"
        }
        '''

        with open("test2.json", "r") as test_data:
            with patch("urllib.request.urlopen") as mocked_get_cases:
                mocked_get_cases.return_value = test_data
                self.assertEqual(what_is_year_now(), 2019)

    def test_what_is_year_now_3(self):
        '''
        Тест выполнения неверного формата DD.MM.YYYY

        Исходные данные для теста

        {
            "$id": "1",
            "currentDateTime": "первое января 2022"
        }
        '''

        with open("test3.json", "r") as test_data:
            with patch("urllib.request.urlopen") as mocked_get_cases:
                mocked_get_cases.return_value = test_data
                with self.assertRaises(ValueError):
                    what_is_year_now()

    def test_what_is_year_now_4(self):
        '''
        Тест на наличие ключа currentDateTime

        Исходные данные для теста

        {
            "$id": "1",
            "WrongAttribute": "2022-10-02T18:55Z"
        }
        '''

        with open("test4.json", "r") as test_data:
            with patch("urllib.request.urlopen") as mocked_get_cases:
                mocked_get_cases.return_value = test_data
                with self.assertRaises(KeyError):
                    what_is_year_now()


if __name__ == '__main__':
    year = what_is_year_now()
    exp_year = 2022

    print(year)
    assert year == exp_year
