from gramatica_crud import generar_gramatica_crud


def mostrar_gramatica():
    g = generar_gramatica_crud()

    print("== No terminales ==")
    print(", ".join(g.no_terminales))
    print()

    print("== Terminales ==")
    print(", ".join(g.terminales))
    print()

    print("== Producciones ==")
    for p in g.producciones:
        derecha = " ".join(p.right) if p.right else "ε"
        print(f"{p.left} → {derecha}")
    print()

    print("== Atributos por símbolo ==")
    for nt, attrs in g.atributos.items():
        print(f"{nt}: {attrs}")
    print()

    print("== Reglas de atributos ==")
    for r in g.reglas_atributos:
        print(f"{r.produccion}")
        print(f"   {r.regla}")
    print()


