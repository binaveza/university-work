classes = [
    'Person',
    'Employee'
]

clss = []
clss.append(type(classes[0],
               (),
               {
                   '__init__': lambda self, name: setattr(self, 'name', name),
                   '__str__': lambda self: f"Name: {self.name}",
               })
            )

clss.append(type(classes[1],
               (clss[0], ),
               {
                   '__init__': lambda self, name, position:
                    clss[0].__init__(self, name) or setattr(self, 'position', position),
                   '__str__': lambda self: f"Name: {self.name}\nPosition: {self.position}",
               })
    )
e1 = clss[1]("Ivan Doberman", "Boss")
print(e1, e1.__class__.__name__)

p1 = clss[0]("Baba Valya")
print(p1, p1.__class__.__name__)