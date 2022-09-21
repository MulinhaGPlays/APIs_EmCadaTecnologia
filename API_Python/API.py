import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'HomePage'

@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('DadosDaAPI.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)

app.run(host='0.0.0.0')