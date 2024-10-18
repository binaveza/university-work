from pygments.lexers import func

f = '''def func(x, y):
    return x + y
'''

exec(f)
print(func(1,2))
print(func, type(func))