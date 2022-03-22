class ComputerPart(): 
    def __init__ (self,pabrikan,harga):
        self.pabrikan = pabrikan 
        self.harga = harga 
    
    def display(self):
        print("Pabrikan : ",self.pabrikan) 
        print("Harga    : ", self.harga,"\n")

class Processor(ComputerPart): 
    def __init__(self,nama,jumlah_core,speed):
        self.nama = nama 
        self.jumlah_core = jumlah_core 
        self.speed = speed 

    def display(self): 
        print("Nama Processor : ",self.nama)
        print("jumlah core    : ",self.jumlah_core)
        print("Speed          : ", self.speed)


processor_1 = ComputerPart("Intel", 6000000)
processor_1.display()


processor_2 = Processor("Intel Core i7",6,"2.4 Ghz")
processor_2.display()