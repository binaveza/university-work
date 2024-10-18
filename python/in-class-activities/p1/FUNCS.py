FUNCS = {
    '1': {
        'name': 'add',
        'op': '+'
    },
    '2': {
        'name': 'sub',
        'op': '-'
    },
    '3': {
        'name': 'mul',
        'op': '*'
    },
    '4': {
        'name': 'div',
        'op': '/'
    },
}

for k in FUNCS:
    f = f'''
def {FUNCS[k]['name']}(x, y):
    return x {FUNCS[k]['op']} y
'''
    code = compile(f, "my_module", "exec")
    exec(f)

print(add(2, 5))
print(sub(2, 5))
print(mul(2, 5))
print(div(2, 5))