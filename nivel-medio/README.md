
# Projeto Flask com SQLite

Este projeto é uma API simples construída com Flask e SQLite. Ele permite salvar, recuperar e limpar dados de usuários em um banco de dados SQLite.

## Pré-requisitos

- Python 3.x instalado no sistema

- Pip (gerenciador de pacotes do Python)


## Instalar as Dependências

Instale as dependências necessárias globalmente:

    pip  install  Flask  requests


### Executar  a  API

Para  iniciar  o  servidor  Flask,  execute  o  seguinte  comando:  

    python  api.py

A  API  estará  disponível  em  http://127.0.0.1:5000.

### Endpoints  da  API

1.  Salvar  Usuários
 - URL:  /api/usuarios
- Método:  POST
- Descrição:  Salva  uma  lista  de  usuários  no  banco  de  dados.


2.  Recuperar  Usuários
- URL:  /api/usuarios
- Método:  GET
- Descrição:  Recupera  todos  os  usuários  do  banco  de  dados.

3.  Limpar  Usuários
- URL:  /api/usuarios/limpar
- Método:  DELETE
- Descrição:  Remove  todos  os  usuários  do  banco  de  dados.

### Executar  o  Script  de  Limpeza  e  Inserção

Para  limpar  e  inserir  dados  na  API,  execute  o  seguinte  comando:

    python  clean_insert.py

  

### Executar  o  Script  de  Limpeza  do  Banco  de  Dados

Para  limpar  todos  os  dados  do  banco  de  dados,  execute  o  seguinte  comando:

    python  clean_users.py
