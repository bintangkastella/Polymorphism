class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama 
        self.nim = nim 
       

    def tampilMhs(self): 
        print("Nama : ", self.nama, ", nim : ", self.nim)
    
   
    def HitungSKS(self, jmlsks = None , sks = None): 
        if jmlsks != None and sks != None:
            totalsks = jmlsks +sks
            print("Total sks : ",totalsks) 
        else:
            totalsks = jmlsks
            print("Total sks : ", totalsks) 


mhs1 = Mahasiswa ("Gojo" , 534323142) 
mhs2 = Mahasiswa ("Toji", 12347854)
mhs1.tampilMhs() 
mhs2.tampilMhs()
mhs1.HitungSKS(87, 33) 
mhs2.HitungSKS(90)
