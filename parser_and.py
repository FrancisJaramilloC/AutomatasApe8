"""
Nivel 2 (AND): Term -> Term & Factor | Factor
Autor: Joel Tapia
"""

# Term -> Factor ( '&' Factor )* — asociatividad izquierda.
def parse_term(token_actual, avanzar, parse_factor):
    # Llama al nivel inferior (NOT/ID)
    nodo = parse_factor()

    # Mientras encuentre el operador AND
    while token_actual() == "&":
        avanzar() # Consume el '&'
        
        # Validar que después del '&' venga algo válido
        if token_actual() is None or token_actual() in ["|", "&", ")"]:
            raise ValueError("Error de sintaxis: Falta operando despues del AND")
            
        derecho = parse_factor()
        nodo = ("AND", nodo, derecho)

    return nodo