class grandparent:
    def property(self):
        print("has property")
                                          #single inheritance
class parent(grandparent):
    def money(self):
        print("has money")
        
# __________________________________      #multilevel inheritance
        
class child1(parent):
    def car(self):
        print("has car")
        
class child2(parent):
    def bike(self):
        print("has bike")
        
obj1 = child1()
obj2 = child2()

obj1.property()
obj1.money()
obj1.car()

print("________________________")


obj2.property()
obj2.money()
obj2.bike()