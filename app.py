from flask import Flask, request, jsonify, render_template
from lexer import lexer
from parser import parser  # Importa el parser desde parser.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form['code']
    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append({
            'type': tok.type,
            'value': tok.value,
            'line': tok.lineno,
            'position': tok.lexpos
        })
    
    try:
        result = parser.parse(code)
        if result is None:
            result = "Estructura FOR incorrecta"
    except Exception as e:
        result = f"Error de análisis: {e}"

    return jsonify({
        'tokens': tokens,
        'result': result
    })

@app.errorhandler(500)
def internal_error(error):
    response = jsonify({
        'error': 'Internal Server Error',
        'message': str(error)
    })
    response.status_code = 500
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    response = jsonify({
        'error': 'Exception',
        'message': str(e)
    })
    response.status_code = 500
    return response

if __name__ == '__main__':
    app.run(debug=True)
