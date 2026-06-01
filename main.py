import re
from parser_or import parse_exp              # Francisco (feature/or)
# from parser_and import parse_term          # Joel (feature/and) — descomentar al integrar
# from parser_not import parse_factor        # Alexander (feature/not) — descomentar al integrar

# Tokens
TOKEN_NOT    = "TOKEN_NOT"
TOKEN_AND    = "TOKEN_AND"
TOKEN_OR     = "TOKEN_OR"
TOKEN_LPAREN = "TOKEN_LPAREN"
TOKEN_RPAREN = "TOKEN_RPAREN"
TOKEN_ID     = "TOKEN_ID"
TOKEN_EOF    = "TOKEN_EOF"

# Simbolos fijos
SIMBOLOS_FIJOS = {
    "~": TOKEN_NOT,
    "&": TOKEN_AND,
    "|": TOKEN_OR,
    "(": TOKEN_LPAREN,
    ")": TOKEN_RPAREN,
}

# Lexer
REGEX_ID = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*") #Todos los datos que soporta el analizador
REGEX_ESPACIOS = re.compile(r"[ \t\n\r]+") #Espacios en blanco que no se soportan

#Identificar los tokens y analizador lexico
def lexer(expresion):
    resultado = []
    i = 0
    while i < len(expresion):
        match = REGEX_ESPACIOS.match(expresion, i)
        if match:  #Elimina los espacios en blanco
            i = match.end()
            continue
        c = expresion[i] 
        if c in SIMBOLOS_FIJOS:  #Identifica los simbolos fijos
            resultado.append((SIMBOLOS_FIJOS[c], c))
            i += 1
            continue
        match = REGEX_ID.match(expresion, i)
        if match: #En caso de que no se encuentre un simbolo fijo se busca un id 
            resultado.append((TOKEN_ID, match.group()))
            i = match.end()
            continue
        raise ValueError(f"Error lexico: caracter inesperado '{c}' en posicion {i}")
    resultado.append((TOKEN_EOF, None))
    return resultado

# Estado del parser
tokens = []
posicion = 0

#Retorna el token actual
def token_actual():
    if posicion < len(tokens):
        return tokens[posicion][1]
    return None

#Avanza a la siguiente posicion
def avanzar():
    global posicion
    posicion += 1

# Punto de entrada
def parsear(expresion):
    global tokens, posicion
    tokens = lexer(expresion)
    posicion = 0
    # Al integrar: parse_exp llama a parse_term, que llama a parse_factor
# Conectar los 3 niveles: OR -> AND -> NOT -> (OR)
#   _factor = lambda: parse_factor(token_actual, avanzar, _exp)
#    _term = lambda: parse_term(token_actual, avanzar, _factor)
    _exp = lambda: parse_exp(token_actual, avanzar, _term)

    resultado = _exp()
    if token_actual() is not None:
        raise ValueError(f"Error de sintaxis: token inesperado '{token_actual()}'")
    return resultado

if __name__ == "__main__":
    print("Parser de Expresiones Booleanas\n")
    while True:
        entrada = input(">> ")
        if entrada.strip().lower() == "salir":
            break
        if not entrada.strip():
            continue
        try:
            print(f"AST: {parsear(entrada)}\n")
        except ValueError as e:
            print(f"{e}\n")
