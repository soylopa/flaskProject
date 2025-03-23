from flask import Flask, render_template
from datetime import datetime
import csv
from jinja2 import Template

app = Flask(__name__)


@app.add_template_global
def today(date):
    return date.strftime('%d-%m-%Y')

def get_first_friend(friends):
    
    for friend in friends:
        return friend

@app.route('/hello2')
def hello():
    friends = ['Robin', 'Caro', 'Nestor', 'Diego', 'Paola']
    date = datetime.now()
    name = get_first_friend(friends)
    return render_template(
        'hello.html',
        name = name,
        date = date,
        )

@app.route('/rutas/<name>')
def hello(id = None, name = None, surname = None):
    my_data = {
        'name' : name,
        'surname': surname,
        'id' : id
    }
    if name == None and id == None:
        return render_template('hello.html', data = my_data)