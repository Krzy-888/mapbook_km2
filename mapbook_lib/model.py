from dataclasses import dataclass, field
from typing import List


@dataclass
class User:
    name: str
    location: str
    posts: List[str] = field(default_factory=list)


users: List[User] = [
    User(name="Artur", location="Łomża",
         posts=["Sprzedam mercedesa", "Kupie skrzynie biegow", "Ratunku co robić po wypadku?",
                "Kto dzisiaj idzie biegać?"]),
    User(name="Daniel", location="Legionowo",
         posts=["Moj kod nie dziala, pomocy!"]),
    User(name="Kamil", location="Ciechanów",
         posts=["Czy ktoś już zrobił sprawozdanie z PPyth?"]),
]
