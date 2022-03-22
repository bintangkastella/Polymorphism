from abc import ABC, abstractmethod 
class Bentuk(ABC):
    @abstractmethod
    def luas(self): 
        return self.__sisi * self.__sisi

    @abstractmethod
    def Keliling(self): 
        return 4 * self.__sisi 


class Persegi(Bentuk):
    def __init__(self,sisi):
        self.__sisi = sisi 
    def luas(self): 
        return self.__sisi * self.__sisi 
    def Keliling(self):
        return 4 * self.__sisi

persegi = Persegi(6)  
print(persegi.luas())
print(persegi.Keliling())