#wed

from flask import Flask

app = Flask(__name__)

@app.route('/')

def inicio():
    
    return 'Bem Vindos ao mundo real meus quiridus'

app.run()
