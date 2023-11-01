import pandas as pd
from app import consultar_tempo, criar_tabela, conectar_db, iniciar_flask
import sqlite3
import requests 


def teste_consultar_tempo():
    tempos = consultar_tempo()
    assert isinstance(tempos, list) 
    assert len(tempos) == 11  
    
def teste_criar_tabela():
    tabela = criar_tabela()
    assert isinstance(tabela, pd.DataFrame) 
    
def teste_conectar_db():
    resultado = conectar_db()
    assert isinstance(type(resultado), type(sqlite3.Cursor)) 
    
iniciar_flask()
def testar_flask_obter_tempo():
    resultado_request = requests.get('http://127.0.0.1:5000/tempo')
    assert resultado_request.status_code == 200  
    json = resultado_request.json()  
    assert json  
