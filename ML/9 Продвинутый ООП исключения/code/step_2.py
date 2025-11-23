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


def create_product(name, price):
    # product = Product(name, price)
    # return product
    try:
        5 / 0
        product = Product(name, price)
        return product
    except Exception as e:
        # print(e)
        raise WrongPriceValue(e)


try:
    # product_1 = create_product('RedmiNote 10', 1478)
    product_1 = create_product('RedmiNote 10', '1478 rub')
    print(product_1)
except WrongPriceValue as e:
    print(f'entered wrong price: {e.args}')
    exit(2)
