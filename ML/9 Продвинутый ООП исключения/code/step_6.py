class MyStr(str):
    def __add__(self, other):
        # return f'{self}{other}'
        return MyStr(f'{self}{other}')


a = 5
# b = '5'
b = MyStr(5)
# print(a + b)
print(b + a)
print(b + a + a)
