from code_flask import app
from flask import render_template

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Homepage')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html', title='Projetos')

@app.route('/contato')
def contato():
    return render_template('contato.html', title='Contato')