from flask import Flask, request, jsonify
from flask_cors import CORS
import main  # Importa tu archivo main.py

app = Flask(__name__)
CORS(app) # Permite peticiones desde el navegador

@app.route('/api/parse', methods=['POST'])
def parse_api():
    datos = request.get_json()
    expresion = datos.get('expresion', '')
    
    try:
        # Usamos tu lexer para obtener los tokens
        tokens_generados = main.lexer(expresion)
        
        # Usamos tu parser para obtener el árbol (AST)
        arbol_generado = main.parsear(expresion)
        
        # Convertimos las tuplas de Python a listas (JSON no soporta tuplas)
        def tuple_to_list(t):
            if isinstance(t, tuple):
                return [tuple_to_list(x) for x in t]
            return t
            
        arbol_serializado = tuple_to_list(arbol_generado)

        return jsonify({
            'tokens': tokens_generados,
            'ast': arbol_serializado
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    print("Servidor web levantado en http://127.0.0.1:5000")
    app.run(debug=True)