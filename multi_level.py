class grandparent:
    def property(self):
        print("has property")

class father(grandparent):
    def money(self):
        print("has money")
        
        
class child(father):
    def love(self):
        print("has car")
        
obj = child()

obj.property()
obj.money()
obj.love()