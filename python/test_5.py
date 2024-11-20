# class D():
#     d = 100,

# obj = D()

# result = getattr(D, 'd')

# print(result)



class A:
    __a = 0

    def deco(func):

        def wrapper(*args):
            func(*args)

        return wrapper

namespace = A.__dict__

print(namespace)
