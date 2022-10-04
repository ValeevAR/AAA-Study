import json
from collections.abc import Iterable


# class for dynamic creation of sub attributes
class SubAdvert:
    def __init__(self, advert):
        self.advert = advert

    # dynamic creation of sub attributes
    def __getattr__(self, item):
        # code for task 1.2
        if item == 'price' and item not in self.advert:
            return 0

        # use of recursion for dynamic creation of attributes
        if isinstance(self.advert[item], Iterable) and not isinstance(self.advert[item], str):
            return SubAdvert(self.advert[item])
        else:
            return self.advert[item]


# Mixin class. It changes standard color into custom one
class ColorizeMixin:
    def __str__(self):
        return f"\033[{self.repr_color_code}m{self.__repr__()}"


class Advert(ColorizeMixin, SubAdvert):
    def __init__(self, *args):
        self.repr_color_code = 32

        # check if input data is not json format. If not, then transform data to {"title":x, "price":x}
        if len(args) == 1:
            advert_data = args[0]
        elif len(args) == 2:
            advert_data = {'title': args[0], 'price': args[1]}

        # loads parent class for dynamic creation of sub attributes
        super().__init__(advert_data)

        # a test if price is lower 0.
        # Probable, "raise" can be here, but it is not evident from the task
        if self.price < 0:
            print('ValueError must be >= 0')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    # test for task 1.1
    lesson_str = """{
    "title": "python", "price": 0,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    print(lesson_ad.title)
    print(lesson_ad.price)
    print(lesson_ad.location.address)

    # test for task 1.2 (part 1)
    lesson_str = """{
       "title": "python", "price": -999,
       "location": {
       "address": "город Москва, Лесная, 7",
       "metro_stations": ["Белорусская"]
       }
       }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    # test for task 1.2 (part 2)
    lesson_str = """{
       "title": "python", 
       "location": {
       "address": "город Москва, Лесная, 7",
       "metro_stations": ["Белорусская"]
       }
       }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)

    # test for task 2
    print(lesson_ad)
    iphone_ad = Advert('iPhone X', 100)
    print(iphone_ad)
