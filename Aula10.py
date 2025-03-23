# Encapsulamento

class Foo\
  :
    def __init__(self):
        self.public = "Isso é público"
        self._protected = "Isso é protegido"
    
    def metodo_publico(self):
        return "metodo_pulico"
    
    def _metodo_protected(self):
        return "_metodo_protected"

f = Foo()
print(f.public, f.metodo_publico(), f._metodo_protected(), sep="\r\n")
