#Обёртка
def strict(func):
    def wrapper(*args):
        print('\n1')

        res = func(*args)

        print('2\n')

        return res
    return wrapper

#Декоратор сначала отрабатывает
@strict
def func(x: int, y: int) -> int:
    return x * y

def func0():
    pass

print(func(5, 3))
print(func('5', 3))

#      это словарь ↓
print(func.__annotations__)
# print(func(print, 3))
