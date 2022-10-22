import json
from collections.abc import Iterable


# class for dynamic creation of sub attributes
class SubAdvert:
    def __init__(self, advert):
        self.advert = advert

    # dynamic creation of sub attributes
    def __getattr__(self, item0):
        # code for task 1.2

        if item0 == 'class_':
            item = 'class'
        elif item0 == '_price':
            item = 'price'
        else:
            item = item0

        if item == 'price' and item not in self.advert:
            return 0

        # use of recursion for dynamic creation of attributes
        if isinstance(self.advert[item], Iterable) and not isinstance(self.advert[item], str):
            return SubAdvert(self.advert[item])
        else:
            return self.advert[item]


# Mixin class. It changes standard color into custom one
class ColorizeMixin():
    def __repr__(self):
        s = f'{self.title} | {self.price} ₽'
        return f"\033[{self.repr_color_code}m{s}"


class Advert(ColorizeMixin, SubAdvert):
    def __init__(self, *args):

        self.repr_color_code = 32
        self.__repr__ = super(Advert, self).__repr__

        # check if input data is not json format. If not, then transform data to {"title":x, "price":x}
        if len(args) == 1:
            advert_data = args[0]
        elif len(args) == 2:
            advert_data = {'title': args[0], 'price': args[1]}

        super().__init__(advert_data)

        # check if price is lower 0
        self.price = self.price

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    @property
    def price(self):
        return self._price

    # a test if price is lower 0.
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('must be >= 0')
        self._price = value


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
    # lesson_str = """{
    #    "title": "python", "price": -999,
    #    "location": {
    #    "address": "город Москва, Лесная, 7",
    #    "metro_stations": ["Белорусская"]
    #    }
    #    }"""
    #
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)

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

    lesson_ad.price = 5
    print(lesson_ad.price)

    # lesson_ad.price = -3
    # print(lesson_ad.price)

    print(iphone_ad.__repr__())

    # test with class_
    lesson_str = """{
       "title": "python", 
       "class": "class_value",
       "location": {
       "address": "город Москва, Лесная, 7",
       "metro_stations": ["Белорусская"]
       }
       }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.class_)
