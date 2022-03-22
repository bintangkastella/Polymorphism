class Mahasiswa():   
    def __init__(self,nama,nim):
        self.nama = nama 
        self.nim = nim 
    
    def detSiswa(self):
        print(self.nama, "alamat : Ukraina")

class Siswa(Mahasiswa):
    def __init__(self,jurusan,nim):
        self.jurusan = jurusan 
        self.nim = nim
    def detSiswa(self):
        print(self.jurusan,"Jurusan :Teknik Nuklir") 

#Membuat objek
mhs1 = Siswa("Magatah", 135105)
mhs2 = Mahasiswa("Shadis", 135119)

print(mhs1.nim, mhs2.nama) 
mhs1.detSiswa() 
print(mhs1.nim, mhs2.nama) 
mhs2.detSiswa() 
