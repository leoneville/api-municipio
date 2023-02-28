# Api Municipios
### 1 - Requisitos para rodar a aplicação
  1. Ter o Docker instalado e configurado na maquina.
  2. Ter o Python instalado e configurado na maquina.
  
### 2 - Preenchendo o arquivo .ENV
Renomeie o arquivo .env.example para .env e preencha as variáveis de ambiente com suas credenciais.<br/>
Na variável de ambiente `FLASK_APP=` coloque o nome do arquivo utilizado para iniciar o projeto.<br/>

### 3 - Comandos para rodar o projeto
Abra o terminal e digite os seguintes comandos:
  1. `docker-compose up -d`
  2. `pip install -r requirements.txt`
  3. `python .\main.py`
  
### 4 - Comandos para a criação das migrations no banco
  Abra um novo terminal e digite os seguintes comandos:
  1. `flask db init` - Isso criará a pasta migrations.
  2. `flask db migrate` - Com isso, as mudanças nos modelos serão detectadas e um novo arquivo será criado na pasta versions.
  3. `flask db upgrade` - Isso aplicará as mudanças detectadas.
  
### 5 - Criando os dados de teste no banco de dados:
  Dentro do diretório SQL, você encontrará um arquivo chamado: <b>dados.sql</b>.<br/>
  Neste arquivo contém o script de criação dos dados teste para rodar dentro do banco de dados.

# Documentação da API
Para acessar a documentação da API, acesse a URL: `http://127.0.0.1:5000/docs/swagger`
