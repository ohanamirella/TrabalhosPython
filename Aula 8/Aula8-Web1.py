# Aula 8 - 18-11-2019
# Web

from flask import Flask

app = Flask(__name__)
@app.route('/')
def inicio():
    return 'Bem vindos ao mundo real meus quiridus'

app.run(host='192.168.0.120', port=80)