from dataclasses import dataclass
@dataclass(init=False, repr=True, eq=True)
class Localidad:
    nombre: str
    codigo_postal: int
    provincia: str
   # pais: str
    

    
   