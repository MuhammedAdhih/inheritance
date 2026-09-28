class father:
    def money(self):
        print("has money")
        
class mother:
    def care(self):
        print("has care")
        
class child(father,mother):
    def love(self):
        print("has love")
        
obj = child()
obj.money()   #}
obj.care()      #accessing both class
obj.love()