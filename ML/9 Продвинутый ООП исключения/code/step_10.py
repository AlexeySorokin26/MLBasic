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


class Basket:
    def __init__(self):
        self._products = {}

    def __str__(self):
        return f'{self._products}'

    def __len__(self):
        return sum(self._products.values())

    def __getitem__(self, item):
        return self._products.get(item)

    def __setitem__(self, key, value):
        self._products[key.name] = value

    def __iter__(self):
        return (el for el in self._products.keys())

    def __contains__(self, item):
        return item in self._products


prod_1 = Product('RedmiNote 10', '1478')
prod_2 = Product('Huawei P50', 2677)
prod_3 = Product('Apple Watch 8', 2317)

user_basket = Basket()
user_basket[prod_1] = 2
user_basket[prod_2] = 3
user_basket[prod_3] = 1

print(user_basket)
print(len(user_basket))
print(user_basket['RedmiNote 10'])
print(user_basket['RedmiNote 10+'])

print('RedmiNote 10' in user_basket)
print('RedmiNote 10+' in user_basket)

for el in user_basket:
    print(el)
