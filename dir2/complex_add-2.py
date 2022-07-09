class add_complex():
    def __init__(self,complex):
        self.c = complex

    def __add__(self, other):
        return self.c + other.c

o1 = add_complex(complex(4,5))
o2 = add_complex(complex(9,2))

print(o1 + o2)
