## my
## нужно было сделать уникальные
def get_alphabet(*args):
    combined = ''.join(args)
    sort = ''.join(sorted(combined))
    return sort

result = get_alphabet("apple", "banana")
print(result)

## teacher

def et_alphabet(*args):
    alph = set()
    for s in args:
        alph = alph.union(set(s))
    res = "".join(sorted(alph))
    return res

s = [
"1. Напишите функцию func(), которая выводит в консоль английский алфавит в виде строки и запустите её",
"2. Перепишите функцию так, чтобы она не печатала строку, а возвращала",
"3. Перепишите функцию, чтобы она получала две строки - первую и последнюю букву, и возвращала строку от первой до последней буквы",
"4. Передавайте в функцию первую и последнюю буквы как именованные аргументы start и end",
"5. Используйте значения по умолчанию, чтобы при вызове функции без параметров выводился весь алфавит"
]

print(et_alphabet(*s[:1]))