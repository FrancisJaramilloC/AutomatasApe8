"""
Nivel 1 (OR): Exp -> Exp | Term | Term
Autor: Francisco Jaramillo
"""

#Exp -> Term ( '|' Term )* — asociatividad izquierda.
def parse_exp(token_actual, avanzar, parse_term):
    nodo = parse_term()

    while token_actual() == "|":
        avanzar()
        if token_actual() is None or token_actual() == "|":
            raise ValueError("Error de sintaxis: Falta operando despues del OR")
        derecho = parse_term()
        nodo = ("OR", nodo, derecho)

    return nodo
