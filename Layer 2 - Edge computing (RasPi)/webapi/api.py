from flask import Flask # Funcionalidades básicas de Flask
from flask import render_template   # Para poder mostrar templates HTML

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    # Mostramos el template "index.html"
    return render_template('index.html')

# Sensor measurements page
@app.route('/sensors')
def sensors():
    return 'Valores leídos por los sensores'

# Database tables page
@app.route('/tables')
def tables():
    return 'Tablas de la base datos'

# Tasks programming page
@app.route('/program')
def program():
    return 'Programación de tareas'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')