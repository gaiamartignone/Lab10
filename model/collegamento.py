from dataclasses import dataclass


@dataclass
class Collegamento:
    stato1: str
    stato2: str
    _anno: int

    @property
    def s1(self):
        return self.stato1

    @property
    def s2(self):
        return self.stato2

    @property
    def anno(self):
            return self._anno
