## my
def get_inits(surname, name, otchestvo):
    init = f"{name[0]}. {otchestvo[0]}."
    return f"{surname} {init}"


surname = "Иванов"
name = "Иван"
otchestvo = "Иванович"

res = get_inits(surname, name, otchestvo)
print(res)

## teacher

def get_inits(**kwargs):
    option = ""
    if kwargs.get('fname'):
        option = kwargs['fname'][0:1] + '.'

    s = f"{kwargs['lname']} " \
        f"{kwargs['name'][0:1]}."\
        f"{option}"

    return s

print(get_inits(name="Nikolay",
                fname="Nikolayevich",
                lname="Ivanov"))

print(get_inits(name="Jane",
                lname="Haelly"))
