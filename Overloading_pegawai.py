class Pegawai: 
    jumlah = 0 

    def __init__(self, nama, gaji):
        self.nama = nama 
        self.gaji = gaji 
        Pegawai.jumlah +=1

    def tampilJumlah(self): 
        print("Total pegawai : ",Pegawai.jumlah)

    def tampilPegawai(self): 
        print("Nama : ", self.nama, ", gaji : ", self.gaji) 

   
    def tunjangan(self, istri = None, anak = None):
        if anak != None and istri != None:
            
            total = anak + istri
            print("Tunjangan anak dan istri : ", total) 

        else: 
            total = istri
            print("Tunjangan istri = ", total)


peg1  = Pegawai("Atta", 2000)
peg2 = Pegawai ("Aurel", 6000)
peg1.tampilPegawai()
peg2.tampilPegawai()
peg1.tunjangan(2500,2000) 
peg2.tunjangan(2500)     

print("Total pegawai %d" % Pegawai .jumlah)
rataGaji = (peg1.gaji + peg2.gaji)/Pegawai.jumlah
print("Rata - rata gaji : "+str(rataGaji)) 