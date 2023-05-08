class Xodim:
    def __init__(self, xname,xage, xmaosh):
        self.ismi = xname
        self.yoshi = xage
        self.maoshi = xmaosh
        
    def print(self):
        print(self.ismi, self.yoshi, self.maoshi)
    
class Ishchilar(Xodim):
   def __init__(self, xname,xage, xmaosh, sogliqni_saqlash, pensiya):
       super().__init__(xname,xage, xmaosh) 
       self.sogliqni_saqlash = sogliqni_saqlash
       self.pensiya = pensiya
       
   def print(self):
       print(self.ismi, " ", "sog'liqni saqlash imtiyoziga ", self.sogliqni_saqlash, " va ", "Pensiya imtiyoziga ", self.pensiya)
    
a = Ishchilar("Aziza", 24, 5000000, "ega", "ega") 
b = Ishchilar("Ulug'bek", 35, 1200000, "ega emas", "ega emas") 
a.print()
b.print()

