from dataclasses import dataclass, field
from builtins import property
from typing import List


@dataclass
class Property:
    name: str
    link: str
    locality: str
    price: str
    images: List[str] = field(default_factory=list, repr=False)

    @property
    def uid(self):
        return self.link
