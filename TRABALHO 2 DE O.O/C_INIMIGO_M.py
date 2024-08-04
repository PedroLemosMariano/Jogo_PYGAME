from CA_CARGAS import *
from VAR_GLOBAL import *
from C_INIMIGO_BASE import *

class InimigoMorcego(InimigoBase):
    def __init__(self, x, y, size, spd, cor):
        imagens = {
            'frente': Morcego_frente,
            'costa': Morcego_costa,
            'ladoD': Morcego_ladoD,
            'ladoE': Morcego_ladoE,
        }
        super().__init__(x, y, size, spd, cor, imagens)