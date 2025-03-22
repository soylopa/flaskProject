from flask import Flask, render_template
from datetime import datetime
import csv
from jinja2 import Template

app = Flask(__name__)

app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

def get_first_friend(friends):
    
    for friend in friends:
        return friend  # Devuelve el primer elemento y termina la función
    
@app.route('/hello')
def hello():
    friends = ['Robin', 'Caro', 'Nestor', 'Diego', 'Paola']
    date = datetime.now()
    name = get_first_friend(friends)
    return render_template(
        'index.html',
        name = name,
        date = date,
        )

@app.route('/hello/<nombre>')
def crear_valores_jinja(linea):
    id = linea[0]
    nombre = linea[1]
    valores = {
        "id" : id,
        "nombre" : nombre
    }
    return valores
def crear_config_jinja(plantilla, valores):
    with open(plantilla, 'r') as j:

        plantilla_jinja = Template(j.read())
        jinja_data= plantilla_jinja.render(valores)

    archivo = 'Template' + valores["id"] + '.html'
    with open(f'templates/{archivo}', 'w') as file:
        for line in jinja_data:
            file.write(line)
def main():
    with open('familia.csv', 'r') as data:
        for row in data:
            clean_row = row.replace('\n', '')
            linea = clean_row.split(',')
            if linea[0]!= 'nombre':
                try:
                    valores = crear_valores_jinja(linea)
                    crear_config_jinja('templates/index.html', valores)
                except:
                    print('Advertencia: problemas con la linea: ', linea)
    print('Trabajo finalizado')
if __name__ == '__main__':
    main()