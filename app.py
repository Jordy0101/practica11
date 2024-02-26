# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola Mundo!, este es un proyecto basico hecho en Flask.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
