import pandas as pd
from datetime import datetime
import requests
from flask import Flask, jsonify
from sqlalchemy import create_engine
import sqlite3
import json


def consultar_tempo():
    cidades = [
        "São Paulo",
        "Rio de Janeiro",
        "Belo Horizonte",
        "Raul Soares",
        "Araçatuba",
        "Fortaleza",
        "Carapicuiba",
        "Rio Casca",
        "Goiânia",
        "São Pedro dos Ferros",
        "foz do iguaçu"
    ]

    url = "https://api.openweathermap.org/data/2.5/weather"

    parametros = {
        "appid": "e44dee71cb605565a151f0ac9e98e478",
        "units": "metric",
    }
    dados = []
    for cidade in cidades:
        parametros["q"] = cidade

        reposta_consulta = requests.get(url, params=parametros)

        if reposta_consulta.status_code == 200:
            dado = reposta_consulta.json()
            dados.append(dado)
        else:
            print("Error:", response.status_code)
    return dados

def criar_tabela():
    data_atual = datetime.now()
    
    valores = consultar_tempo()
    valores = [json.dumps(item) for item in valores]	

    dados_df = {'Data de Ingestão': [data_atual] * 11,
             'Tipo': ["clima São Paulo", "clima Rio de Janeiro", "clima Belo Horizonte", "clima Raul Soares", "clima Araçatuba", "clima Fortaleza", "clima Carapicuiba", "clima Rio Casca", "clima Goiânia", "clima São Pedro dos Ferros", "clima Foz do Iguaçu"],
             'Valores': valores,
             'Uso': ["Previsão_do_tempo", "Previsão_do_tempo", "Previsão_do_tempo", "Previsão_do_tempo", "Previsão_do_tempo", "Previsão_do_tempo", "Previsão_do_tempo", "Previsão_do_tempo", "Previsão_do_tempo", "Previsão_do_tempo", "Previsão_do_tempo"]}

    df = pd.DataFrame(dados_df)

    engine = create_engine('sqlite:///db_atividade.db', echo=False)

    df.to_sql('tabela_tempo', con=engine, if_exists='replace', index=False)
    
    return df

def conectar_db():
    conn = sqlite3.connect('db_atividade.db')
    cursor = conn.cursor()
    return cursor

def iniciar_flask():
    app = Flask(__name__)
    @app.route('/')
    def inciar_api():
        return 'Api flask aberta digite "/tempo" para ver o tempo'
    @app.route('/tempo')
    def obter_tempo():
        criar_tabela()
        conexao = conectar_db()
        conexao.execute("SELECT * FROM tabela_tempo")
        reposta = conexao.fetchall()
        conexao.close()
        return reposta
    if __name__ == '__main__':
        app.run(debug=True, host='127.0.0.1', port=5000)
    return("Api iniciada")
iniciar_flask()
