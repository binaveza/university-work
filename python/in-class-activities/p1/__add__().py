class int_(int):

    def __add__(self, other):
        a = int(self)
        b = int(other)
        return (a + b) * 1.2

    def __eq__(self, other):
        return "self is other and other is self"


a = int_(10)
b = int_(3)

print (a + b)
print (a.__add__(b))
print (a == b)
#print(__add__(a, b))