#Inicializar libreria/dependencias
from flask import Flask
from flask import render_template
from flask import request

import os

app = Flask(__name__)

#rutas
@app.route('/', methods=['GET', 'POST'])
def inicio():
    return render_template('index.html')

#ruta Abaut
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

#ruta Contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

#ruta work
@app.route('/work', methods=['GET', 'POST'])
def work():
    return render_template('work.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port, debug=True)