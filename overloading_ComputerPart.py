class ComputerPart():
    def __init__ (self,jenis):
        self.jenis = jenis
    
    
    def Processor(self, nama = None, harga = None, pabrikan = None): 
        computerpart_3.display_Computer() 
        print("Nama Processor      : ",nama)
        print("Harga               : ",harga)
        print("Pabrikan            : ",pabrikan,"\n") 
    
   
    def RandomAccessMemory(self, nama = None, harga = None, pabrikan = None):
        computerpart_1.display_Computer()
        print("Nama RAM            : ",nama)
        print("Harga               : ",harga)
        print("Pabrikan            : ",pabrikan,"\n")

    
    def HardiskSATA(self, nama = None, harga = None, pabrikan = None):
        computerpart_2.display_Computer()
        print("Nama Hardisk        : ",nama)
        print("Harga               : ",harga)
        print("Pabrikan            : ",pabrikan,"\n")
    
    def display_Computer(self): 
        print("Jenis computer part : ",self.jenis)


computerpart_1 = ComputerPart("Processor")
computerpart_2 = ComputerPart ("RAM")
computerpart_3 = ComputerPart ("Hardisk")


computerpart_1.Processor("INTEL i5 ",1350000,"INTEL")
computerpart_2.RandomAccessMemory("CORSAIR",365000,"CORSAIR")
computerpart_3.HardiskSATA("Hardisk Seagate",410000,"Seagate")