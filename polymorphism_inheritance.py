class processor:
    def intro(self):
        print("Hanya ada 2 jenis processor di dunia yaitu AMD DAN INTEL") 
   
class AMD(processor): 
    def murah(self):
        print("AMD yang menang di harga") 

class INTEL(processor):
    def brand(self):
        print("Intel yang menang di marketing dan image ")

obj_processor = processor()
obj_AMD = AMD()
obj_INTEL = INTEL()

obj_processor.intro() 

\
obj_AMD.intro() 
obj_AMD.murah() 

obj_INTEL.intro() 
obj_INTEL.brand()