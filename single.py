class parent:
    def displayA(self):
        print("parent class")
        
class child(parent):
    def displayB(self):
        print("child class")
        
obj = child()
obj.displayA() #accessing parent class
obj.displayB()