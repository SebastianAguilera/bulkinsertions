from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Especialidad():
    id : int
    nombre : str
