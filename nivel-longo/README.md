
# Projeto Flask com SQLite - Nível Longo - Incompleto

Este projeto é uma API avançada construída com Flask e SQLite. Ele permite salvar, recuperar e limpar dados de usuários em um banco de dados SQLite. O projeto é executado em contêineres Docker.

## Pré-requisitos

- Docker instalado no sistema

- Docker Compose instalado no sistema

  

## Construir e Executar os Contêineres

### Construir a Imagem Docker

 
Navegue até o diretório `nivel-longo` e execute o seguinte comando para construir a imagem Docker:
   

     docker build -t flask-api

  

### Executar os Contêineres com Docker Compose

Execute o seguinte comando para iniciar os contêineres definidos no arquivo docker-compose.yml:

    docker-compose up


### Executar o Script de Limpeza e Inserção

Para limpar e inserir dados na API, execute o seguinte comando dentro do contêiner:

    docker-compose exec flask-api python clean_insert.py

### Executar o Script de Limpeza do Banco de Dados

Para limpar todos os dados do banco de dados, execute o seguinte comando dentro do contêiner:

    docker-compose exec flask-api python clean_users.py
