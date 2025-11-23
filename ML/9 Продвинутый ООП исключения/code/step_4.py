class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = float(price)
        self.__qty = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = float(value)

    def make_dicount(self, pcnt):
        self._price *= (1 - pcnt / 100)

    def __str__(self):
        return f'{self.__class__.__name__}: {self._price}'


class WrongPriceValue(Exception):
    pass


class MyZeroDivisionError(Exception):
    pass


def create_product(name, price):
    product = Product(name, price)
    return product
    # try:
    #     # 5 / 0
    #     product = Product(name, price)
    #     return product
    # except ValueError as e:
    #     # return 'product creation failed'
    #     raise WrongPriceValue(e)
    # except ZeroDivisionError as e:
    #     raise MyZeroDivisionError(e)


try:
    # product_1 = create_product('RedmiNote 10', 1478)
    product_1 = create_product('RedmiNote 10', '1478 rub')
    print(product_1)
except (WrongPriceValue, MyZeroDivisionError) as e:
    print(f'product creation failed: {e.args}')
    exit(2)
except Exception as e:
    print(f'other error: {e}')
    exit(1)
