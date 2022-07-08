class Base:
    def __init__(self):
        print("Base")

class Child1(Base):
    def __init__(self):
        super().__init__()
        print("Child1")

class Child2(Base):
    def __init__(self):
        super().__init__()
        print("Child2")

class Child3(Child1, Child2):
    def __init__(self):
        super().__init__()
        print("Child3")

b = Base()
print("-"*20)
c1 = Child1()
print("-"*20)
c2 = Child2()
print("-"*20)
c3 = Child3()
print(Child3.__mro__)