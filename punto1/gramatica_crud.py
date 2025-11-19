# gramatica_crud.py

from typing import List, Dict
from estructuras_gramatica import GramaticaAtributos, Produccion, ReglaAtributo


def generar_gramatica_crud() -> GramaticaAtributos:
    """
    Genera una gramática de atributos para un mini-lenguaje SQL CRUD.
    """

    no_terminales: List[str] = [
        "Prog", "Consulta",
        "SelectC", "InsertC", "UpdateC", "DeleteC",
        "OptWhere", "LCampo", "Campo",
        "Cond", "Exp", "Valor"
    ]

    terminales: List[str] = [
        "SELECT", "INSERT", "UPDATE", "DELETE",
        "INTO", "VALUES", "SET",
        "FROM", "WHERE",
        "AND", "OR",
        "*", ",", "=", "(", ")",
        "ID", "NUM", "CAD", ";"
    ]

    producciones: List[Produccion] = [

        Produccion("Prog",     ["Consulta", ";"]),
        Produccion("Consulta", ["SelectC"]),
        Produccion("Consulta", ["InsertC"]),
        Produccion("Consulta", ["UpdateC"]),
        Produccion("Consulta", ["DeleteC"]),

        Produccion("SelectC",  ["SELECT", "LCampo", "FROM", "ID", "OptWhere"]),
        Produccion("InsertC",  ["INSERT", "INTO", "ID", "(", "LCampo", ")", "VALUES", "(", "Valor", ")"]),
        Produccion("UpdateC",  ["UPDATE", "ID", "SET", "ID", "=", "Valor", "OptWhere"]),
        Produccion("DeleteC",  ["DELETE", "FROM", "ID", "OptWhere"]),

        Produccion("OptWhere", ["WHERE", "Cond"]),
        Produccion("OptWhere", []),

        Produccion("LCampo",   ["LCampo", ",", "Campo"]),
        Produccion("LCampo",   ["Campo"]),

        Produccion("Campo",    ["ID"]),
        Produccion("Campo",    ["*"]),

        Produccion("Cond",     ["Cond", "AND", "Cond"]),
        Produccion("Cond",     ["Cond", "OR", "Cond"]),
        Produccion("Cond",     ["Exp"]),

        Produccion("Exp",      ["ID", "=", "Valor"]),

        Produccion("Valor",    ["NUM"]),
        Produccion("Valor",    ["CAD"]),
    ]

    atributos: Dict[str, List[str]] = {
        "Prog":     ["cod"],
        "Consulta": ["cod"],
        "SelectC":  ["cod"],
        "InsertC":  ["cod"],
        "UpdateC":  ["cod"],
        "DeleteC":  ["cod"],
        "OptWhere": ["cod"],
        "Campo":    ["cod"],
        "Cond":     ["cod"],
        "Exp":      ["cod"],
        "Valor":    ["cod"],
        "LCampo":   ["lista"],
    }

    reglas_atributos: List[ReglaAtributo] = [

        ReglaAtributo("Prog → Consulta ';'",
                       "Prog.cod = Consulta.cod"),

        ReglaAtributo("Consulta → SelectC",
                       "Consulta.cod = SelectC.cod"),

        ReglaAtributo("Consulta → InsertC",
                       "Consulta.cod = InsertC.cod"),

        ReglaAtributo("Consulta → UpdateC",
                       "Consulta.cod = UpdateC.cod"),

        ReglaAtributo("Consulta → DeleteC",
                       "Consulta.cod = DeleteC.cod"),

        ReglaAtributo("SelectC → SELECT LCampo FROM ID OptWhere",
                       'SelectC.cod = "SELECT " + LCampo.lista + " FROM " + ID.lexema + OptWhere.cod'),

        ReglaAtributo("InsertC → INSERT INTO ID '(' LCampo ')' VALUES '(' Valor ')'",
                       'InsertC.cod = "INSERT INTO " + ID.lexema + "(" + LCampo.lista + ") VALUES(" + Valor.cod + ")"'),

        ReglaAtributo("UpdateC → UPDATE ID SET ID '=' Valor OptWhere",
                       'UpdateC.cod = "UPDATE " + ID1.lexema + " SET " + ID2.lexema + " = " + Valor.cod + OptWhere.cod'),

        ReglaAtributo("DeleteC → DELETE FROM ID OptWhere",
                       'DeleteC.cod = "DELETE FROM " + ID.lexema + OptWhere.cod'),

        ReglaAtributo("OptWhere → WHERE Cond",
                       'OptWhere.cod = " WHERE " + Cond.cod'),

        ReglaAtributo("OptWhere → ε",
                       'OptWhere.cod = ""'),

        ReglaAtributo("LCampo → LCampo ',' Campo",
                       'LCampo.lista = LCampo1.lista + ", " + Campo.cod'),

        ReglaAtributo("LCampo → Campo",
                       'LCampo.lista = Campo.cod'),

        ReglaAtributo("Campo → ID",
                       "Campo.cod = ID.lexema"),

        ReglaAtributo("Campo → '*'",
                       'Campo.cod = "*"'),

        ReglaAtributo("Cond → Cond AND Cond",
                       'Cond.cod = Cond1.cod + " AND " + Cond2.cod'),

        ReglaAtributo("Cond → Cond OR Cond",
                       'Cond.cod = Cond1.cod + " OR " + Cond2.cod'),

        ReglaAtributo("Cond → Exp",
                       "Cond.cod = Exp.cod"),

        ReglaAtributo("Exp → ID '=' Valor",
                       'Exp.cod = ID.lexema + " = " + Valor.cod'),

        ReglaAtributo("Valor → NUM",
                       "Valor.cod = NUM.lexema"),

        ReglaAtributo("Valor → CAD",
                       "Valor.cod = CAD.lexema"),
    ]

    return GramaticaAtributos(
        no_terminales=no_terminales,
        terminales=terminales,
        producciones=producciones,
        simbolo_inicial="Prog",
        atributos=atributos,
        reglas_atributos=reglas_atributos,
    )
