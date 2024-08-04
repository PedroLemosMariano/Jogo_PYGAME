from CA_CARGAS import *
from VAR_GLOBAL import *
from C_INIMIGO_BASE import *

class InimigoCaveira(InimigoBase):
    def __init__(self, x, y, size, spd, cor):
        imagens = {
            'frente': Caveira_frente,
            'costa': Caveira_costa,
            'ladoD': Caveira_ladoD,
            'ladoE': Caveira_ladoE,
        }
        super().__init__(x, y, size, spd, cor, imagens)