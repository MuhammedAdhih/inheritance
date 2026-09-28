class parent:
    def displayA(self):
        print("parent class")
        
class child1(parent):
    def displayB(self):
        print("child class 1")
    
class child2(parent):
    def displayC(self):
        print("child class 2")
    
        
obj1 = child1()
obj2 = child2()


obj1.displayA() #accessing parent class
obj1.displayB()

obj2.displayA()
obj2.displayC()