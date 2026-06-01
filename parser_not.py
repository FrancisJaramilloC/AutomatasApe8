"""
Nivel 3 (NOT / Factor): Factor -> ~ Factor | ( Exp ) | id
Autor: Alexander Ludeña
"""
import re

def parse_factor(token_actual, avanzar, parse_exp):
    token = token_actual()
    
    # Regla 1: ~ Factor
    if token == "~":
        avanzar() # Consumir el '~'
        # Llamada recursiva para permitir cosas como ~~A
        nodo = parse_factor(token_actual, avanzar, parse_exp)
        return ("NOT", nodo)
        
    # Regla 2: ( Exp )
    elif token == "(":
        avanzar() # Consumir el '('
        # Al encontrar paréntesis, volvemos a evaluar desde el nivel más bajo (OR)
        nodo = parse_exp()
        
        # Verificar que se cierre el paréntesis
        if token_actual() == ")":
            avanzar() # Consumir el ')'
            return nodo
        else:
            raise ValueError(f"Error de sintaxis: Falta paréntesis de cierre ')'. Se encontró '{token_actual()}'")
            
    # Regla 3: id
    elif token is not None and re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", token):
        avanzar() # Consumir el ID
        return ("ID", token)
        
    # Error: Si no es '~', ni '(', ni un ID válido
    else:
        raise ValueError(f"Error de sintaxis: Expresión inválida. Se encontró '{token}'")