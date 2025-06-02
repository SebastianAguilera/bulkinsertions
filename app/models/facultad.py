from dataclasses import dataclass
@dataclass(init=False, repr=True, eq=True)
class Facultad:
  nombre: str