class Analizador:
    def __init__(self, texto):
        self.texto = texto.replace(" ", "")
        self.posicion = 0

    def obtener_actual(self):
        if self.posicion < len(self.texto):
            return self.texto[self.posicion]
        return None

    def avanzar(self):
        self.posicion += 1

    # Factor -> ~ Factor | id
    def factor(self):
        actual = self.obtener_actual()

        # Caso NOT (~)
        if actual == "~":
            print("Se encontró NOT (~)")
            self.avanzar()
            return self.factor()

        # Caso id
        elif self.texto[self.posicion:self.posicion + 2] == "id":
            print("Se encontró id")
            self.posicion += 2
            return True

        return False


# Entrada 
cadena = input("Ingrese una expresión lógica: ")

analizador = Analizador(cadena)

# Validación
if analizador.factor() and analizador.posicion == len(cadena.replace(" ", "")):
    print("Cadena válida")
else:
    print("Cadena inválida")