from debugpy.launcher.debuggee import process


class int_(int):

    def __add__(self, other):  # def __add__(self, other)
        a = str(self)
        b = str(other)
        return a + ' and ' + b

    def sum(seq):  # ->  10, 3, 6 and 9

        seq = list(map(str, seq))

        s = ""

        if seq:
            s = seq[0]

            for i in seq[1:-1]:
                s += ", " + i
            if len(seq) > 1:
                s += " and " + seq[-1]

        return s

    def apply(obj, func):

        d = {
            "<class 'list'>": {
                'sum': int_.sum,
            },
        }

        obj_type = str(type(obj))
        conc_func = func.__name__

        process_obj_type = d.get(obj_type)
        if process_obj_type:
            process_func = d[obj_type].get(conc_func)
            if process_func:
                res = process_func(obj)
            else:
                res = "ERROR: Unknown function!\n"
        else:
            res = "ERROR: Unknown object type!\n"

        return res

    def __gt__(self, other):
        return "!"

    def __lt__(self, other):
        return "!"

a = int_(10)
b = int_(3)
c = int_(6)
d = int_(9)

s = [a, b, c, d]

print (a + b)
print(int_.apply(s, sum))
print (b < a)
#print (sum.__dir__())
#print(int_.sum(s))

#print(f"{str(type(list())) = }")
#print(f"{sum.__name__ = }")


#
# i = 10
# ii = 20
#
# print(i + ii)
