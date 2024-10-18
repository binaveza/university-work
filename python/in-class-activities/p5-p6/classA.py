class A(object):
    def __gt__(self, other):
        return "!"

a = A()
b = A()

print(a == b)

print(isinstance(a,(object, )))

print(type(A))

print(object.__dict__)