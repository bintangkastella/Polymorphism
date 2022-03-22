print(len("Polymorphism")) 
print(len([0,1,2,3]))





class Pacar :
    def Hubungan(self): 
        print("Ari adalah pacar dina") 

class Selingkuhan:
    def Hubungan(self):
        print("Zara Selingkuhan Ari")


hub1 = Pacar()
hub2 = Selingkuhan()

for asmara in (hub1,hub2): 
    asmara.Hubungan() 