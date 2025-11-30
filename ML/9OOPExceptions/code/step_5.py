class WrongNum(Exception):
    pass


def get_num():
    num = int(input('max 10: '))
    if num > 10:
        raise WrongNum(num)
    return num


try:
    number = get_num()
except WrongNum as e:
    print(f'wrong num: {e.args}')
else:
    print(f'num is {number}')
