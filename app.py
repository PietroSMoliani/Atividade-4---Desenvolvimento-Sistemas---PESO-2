from flask import Flask, redirect, render_template

app = Flask(__name__)

# -------------------------------------------------------
# Exercício 1 — Página inicial (index)
@app.route('/')
def index():
    return '<h1>Hello, Flask !!</h1>'

