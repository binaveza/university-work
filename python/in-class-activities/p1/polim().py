def func():
    a = [1000, 'ABC']

def func_():
    print(func.name)

func.name = "ABC"
print(func.__name__)
func_()

# print(func)
# print(type(func))
# print(func.__dict__)

r = getattr(func, 'name')
setattr(func, 'name', "XYZ")
r = getattr(func, 'name')
delattr(func, 'name')
print("!", func_)
