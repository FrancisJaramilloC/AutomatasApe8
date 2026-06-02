"""
Nivel 3 (NOT): Factor -> '~' Factor | '(' Exp ')' | id
Autor: Alexander
"""

# Factor -> '~' Factor | '(' Exp ')' | id — recursivo a la derecha para NOT.
def parse_factor(token_actual, avanzar, parse_exp):
    actual = token_actual()

    # Caso NOT (~): unario, recursivo
    if actual == "~":
        avanzar()  # Consume el '~'

        if token_actual() is None:
            raise ValueError("Error de sintaxis: Falta operando despues del NOT")

        operando = parse_factor(token_actual, avanzar, parse_exp)
        return ("NOT", operando)

    # Caso paréntesis: delega al nivel superior (OR)
    elif actual == "(":
        avanzar()  # Consume '('
        nodo = parse_exp()

        if token_actual() != ")":
            raise ValueError("Error de sintaxis: Se esperaba ')' pero se encontro '{}'".format(token_actual()))

        avanzar()  # Consume ')'
        return nodo

    # Caso id: identificador o literal
    elif actual is not None and actual not in ["~", "&", "|", "(", ")", None]:
        avanzar()  # Consume el id
        return ("ID", actual)

    raise ValueError(f"Error de sintaxis: token inesperado '{actual}'")