from dataclasses import dataclass
@dataclass(init=False, repr=True, eq=True)
class Materia:
  nombre: str
  #especialidad: str
  plan: int
  ano: int
  