from flask import Flask, redirect, render_template

app = Flask(__name__)

# -------------------------------------------------------
# Exercício 1 — Página inicial (index)
@app.route('/')
def index():
    return '<h1>Hello, Flask !!</h1>'

# -------------------------------------------------------
# Exercício 2 — Versão do app
@app.route('/versao')
def versao():
    versao = "1.1.0"
    return f"App v{versao}"

# -------------------------------------------------------
# Exercício 3 — Saudação por parâmetro de rota
@app.route('/saudar/<nome>')
def saudar(nome):
    nome_formatado = nome.capitalize()
    return f"Olá, {nome_formatado}!"

