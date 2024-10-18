# Обёртка
def strict(func):
    def wrapper(*args):
        annots = func.__annotations__  # Получаем аннотации
        annots_keys = list(annots.keys())

        if len(annots_keys) - 1 != len(args):
            err_str = f"Function {func.__name__} expects " \
                       f"{len(annots_keys) - 1} parameter{'s' if len(annots_keys) > 2 else ''}, " \
                       f"but {len(args)} is given\n"
            raise TypeError(err_str)

        for i, arg in enumerate(args):
            if not isinstance(arg, annots[annots_keys[i]]):
                err_str = f"Function {func.__name__} expects " \
                          f"{annots[annots_keys[i]]} type, " \
                          f"but {type(arg)} is given instead\n"
                raise TypeError(err_str)

        res = func(*args)
        ret = annots['return']

        if not isinstance(res, ret):
            err_str = f"Function {func.__name__} should return " \
                       f"{ret} type, but tried to return {type(res)} instead\n"
            raise TypeError(err_str)

        return res
    return wrapper

# Декоратор сначала отрабатывает
@strict
def func0(x: int, y: int) -> int:
    return x * y

@strict
def func1(x: str, y: int) -> str:
    return x * y

@strict
def func2(x: int, y: int) -> (int,int,int):
    return x + y, y - x, x > y

# Примеры вызова функции
print("1:", func0(5, 3))  # Должен вернуть 15
print("2:", func1('5', 3))  # Это вызовет ошибку типа \ 555
print("3:", func2(5, 3)) # (8, 2, True)

# Печать аннотаций
#print(func0.__annotations__)
