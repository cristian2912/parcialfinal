# estructuras_gramatica.py

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Produccion:
    """
    A → α
    left:  'A'
    right: ['X1', 'X2', ...]
    """
    left: str
    right: List[str]


@dataclass
class ReglaAtributo:
    """
    Regla de la forma:
        SelectC.cod = "SELECT " + LCampo.lista + ...
    Se deja como texto para efectos de documentación.
    """
    produccion: str   # texto de la producción ejm: "SelectC → SELECT LCampo FROM ID OptWhere"
    regla: str        # texto de la regla semántica


@dataclass
class GramaticaAtributos:
    no_terminales: List[str]
    terminales: List[str]
    producciones: List[Produccion]
    simbolo_inicial: str
    atributos: Dict[str, List[str]]   # p.ej. {'Prog': ['cod'], 'LCampo': ['lista'], ...}
    reglas_atributos: List[ReglaAtributo]
