class Product(object):
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

    def __getattribute__(self, item):
        print(f'__getattribute__: {item}')
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print(f'__getattr__: {item}')
        # return 'Hello'


prod_1 = Product('RedmiNote 10', '1478')
prod_2 = Product('Huawei P50', 2677)
prod_3 = Product('Apple Watch 8', 2317)

# prod_1()
print(prod_1.price)
print(prod_1.super_price)
