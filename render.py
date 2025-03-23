from flask import Flask, render_template
from datetime import datetime
import csv
from jinja2 import Template

app = Flask(__name__)

def crear_valores_jinja(linea):
    id = linea[0]
    nombre = linea[1]
    apellido = linea[2]
    valores = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido
    }
    return valores

def crear_config_jinja(plantilla, valores):
    
        with app.app_context():
            jinja_data = render_template('index.html', **valores)

        archivo = f"Template_{valores['nombre']}.html"
        with open(f'templates/{archivo}', 'w', encoding='utf-8') as file:
            for line in jinja_data:
                file.write(line)
                print(line)

@app.route('/templates/Template_<nombre>.html')
def main():
    with open('familia.csv', 'r') as data:
        for row in data:
            clean_row_t = row.replace('\t','')
            clean_row = clean_row_t.replace('\n', '')
            linea = clean_row.split(',')
            if linea[0] != 'nombre':
                try:
                    valores = crear_valores_jinja(linea)
                    crear_config_jinja('templates/index.html', valores)
                except Exception as e:
                    print(f"Advertencia: problemas con la línea {linea}: {e}")
if __name__ == '__main__':
    main()
