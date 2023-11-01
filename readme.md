# Flask:

Para a atividade foi disponiblizilizada uma API flask local, 

configurada de forma a criar 2 endpoints do tipo Get:

(/) Responsável por fornecer um feedback ao usuário que a API foi aberta

(/tempo) Para consultar a API da Open Weather e obter o clima nas cidades especificadas, informação essa que estará armazenada em um banco de dados sql que será consultado e suas informações devolvidas pela requisição.

# ETL e Armazenamento:

Para a extração dos dados foi utilizada a biblioteca requests para realizar um request na API da API da Open Weather, a fim  de obter o clima das 11 cidades especificidades no código:

São Paulo, Rio de Janeiro, Belo Horizonte, Raul Soares, Araçatuba, Fortaleza, Carapicuiba, Rio Casca, Goiânia, São Pedro dos Ferros, foz do iguaçu

Após a extração dessas informações foram geradas as informações para serem guardadas na tabela:

coluna Data de Ingestão: recebendo a data obtida através da biblioteca datetime, registrando o horário em que as informações foram salvas na tabela

coluna Tipo: Indicando a cidade e o tipo de dados a partir da lista de cidades que foram consultadas na Open Weather ex: "clima São Paulo"

coluna Valores: Essa coluna recebeu os .json obtidos de resposta pelas requisições realizadas na Openweather.

coluna Uso: Foi fornecida uma string para fornecer um exemplo de uso desses dados.

Armazenamento: Por fim, as colunas geradas a partir dos dados mencionados foram utilizadas para criação de um Data Frame pandas e posteriormente subidas para um banco de dados sql.

Consumo flask: O consumo dessas informações será realizado pela API flask criada através do endpoint “/tempo”, que irá consumir os dados do db criado através de um get

# Testes

Foram criados 4 testes para o código 

1- teste da requisição na open weather

2- teste da criação da tabela e envio para o db

3- teste da conexão com bd

4- teste do consumo do db pela API flask

# Como utilizar o codigo

1- instale as dependencias necesarias:

```python
  pip install Flask
  pip3 install --upgrade watchdog
  pip install pandas
  pip install pytest
  pip install sqlalchemy
  pip install requests

```


2- No ubuntu acesse a pasta onde estão os arquivos

3- para iniciar o código utilize o python para rodar o codigo app.py

4- Acesse a API fornecida

5- Utilize "/tempo" para realizar a requisição para obter as informações sobre o tempo de 11 cidades diferentes.

# Como realizar os testes: 

1- instale as dependências necessárias mencionadas acima

2- No ubuntu acesse a pasta onde estão os arquivos

3- Utilize o phyton para rodar o codigo app.py para abrir a API flask

4- digite pytest para executar os testes

5- espere os resultados

# Observações:

Digite /tempo para obter as informações de tempo, pode demorar um pouco.

Utilize um ambiente linux ubuntu para rodar, com python e pip devidamente instalados e atualizados


