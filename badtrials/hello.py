from flask import Flask, render_template
from datetime import datetime
import csv
from jinja2 import Template

app = Flask(__name__)

@app.route('/hello')
def crear_valores_jinja(linea):
    id = linea[0]
    nombre = linea[1]
    valores = {
        'id' : id,
        'nombre' : nombre
    }
    return valores
def crear_config_jinja(plantilla, valores):
    try:
        with open(plantilla, 'r') as j:

            plantilla_jinja = Template(j.read())

            print("Valores antes de renderizar:", valores)  # Depuración

            jinja_data= plantilla_jinja.render(valores)

        archivo = 'Template' + valores['id']+ '.html'
        with open(f'templates/{archivo}', 'w') as file:
            file.write(jinja_data)
    except Exception as e:
        print(f"Error al procesar la plantilla con valores {valores}: {e}")
def main():
    with open('familia.csv', 'r') as data:
        for row in data:
            clean_row_t= row.replace('\t', '')
            clean_row = clean_row_t.replace('\n', '')
            linea = clean_row.split(',')
            if linea[0] != 'nombre':
                try:
                    valores = crear_valores_jinja(linea)
                    crear_config_jinja('templates/index.html', valores)
                except Exception as e:
                    print(f"Advertencia: problemas con la línea {linea}: {e}")
    print('Trabajo finalizado')
if __name__ == '__main__':
    main()