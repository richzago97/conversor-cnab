# Documentação do Projeto Conversor CNAB

## Visão Geral
O projeto Conversor CNAB é um desafio proposto pela Kenzie Academy Brasil, que tem como objetivo parsear arquivos de texto CNAB, normalizar as informações e armazená-las em um banco de dados relacional. O projeto é desenvolvido em Python, utilizando o framework Django. Nesta documentação, você encontrará informações sobre como configurar, executar e utilizar o projeto Conversor CNAB.

## Instruções de Entrega do Desafio
Para concluir o desafio do Conversor CNAB, siga as instruções abaixo:

1. Crie um repositório público no GitHub para o projeto.
2. Implemente o projeto localmente, conforme as instruções e especificações a seguir.
3. Faça o push do projeto para o repositório público no GitHub.
4. Envie os links dos seus repositórios no Canvas.

## Sobre o Desafio
O desafio consiste em criar uma aplicação web que permita o upload de arquivos CNAB, faça a interpretação (parse) desses arquivos, normalize as informações e as armazene em um banco de dados relacional. A aplicação deve exibir as informações importadas em uma interface web.

### Funcionalidades Principais
A aplicação do Conversor CNAB deve:

1. Ter uma tela com um formulário para fazer o upload de arquivos CNAB.
2. Interpretar o arquivo recebido, normalizar os dados e salvá-los corretamente em um banco de dados relacional.
3. Exibir uma lista das operações importadas por lojas, incluindo um totalizador do saldo em conta por loja.

### Requisitos Técnicos
A aplicação deve seguir os seguintes requisitos técnicos:

1. Escrita em Python 3.0+.
2. Deve ser de fácil configuração e execução, de preferência dockerizada e funcionando em ambiente Unix (Linux ou Mac OS X).
3. Deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.

### Executando o Projeto
Para executar o projeto Conversor CNAB, siga as etapas abaixo:

1. Clone o repositório do projeto para o seu ambiente de desenvolvimento.
2. Crie um ambiente virtual Python com o comando: `python -m venv venv`.
3. Ative o ambiente virtual com base no seu sistema operacional (Windows ou Linux/Mac OS).
4. Instale as dependências do projeto com o comando: `pip install -r requirements.txt`.
5. Configure as variáveis de ambiente no arquivo .env com as credenciais apropriadas.
6. Execute o comando `python manage.py migrate` para realizar as migrações do banco de dados.
7. Inicie o projeto com o comando `python manage.py runserver`.

## Considerações Finais
O projeto Conversor CNAB é um desafio que testa suas habilidades em Python e no framework Django. Ele permite importar, normalizar e armazenar informações de arquivos CNAB em um banco de dados relacional. O projeto é uma oportunidade de demonstrar sua capacidade de desenvolver aplicações de back-end, lidar com arquivos, banco de dados e apresentar resultados em uma interface web. Certifique-se de seguir as instruções detalhadas e personalizar o projeto de acordo com suas preferências.
