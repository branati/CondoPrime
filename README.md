# PDS 2015.1 - CondoPrime

## Apresentação

Somos alunos do IF do Rio Grande do Norte, do curso de **TADS** (Tecnologia e Análise em Desenvolvimento de Sistemas). Neste semestre (2015.1) estamos cursando a disciplina **PDS Web** (Processo de Desenvolvimento de Software), tendo por objetivo principal desenvolver o Sistema **CondoPrime** (Sistema Gerenciador de Condomínios).

## Componentes

* Armando Filho
* Érik Alexandre
* Gercino Jr
* Ivan Diniz
* Tatiana Dantas

## Professores Monitores

* Fellipe Aleixo (Desenvolvimento de Sistema WEB)
* Marilia Freire (Análise e Projeto Orientados a Objeto)
* José Antônio (Banco de Dados)

# CondoPrime
Aplicativo para gestão de condominios.

## Instalação
Para instalar o ambiente, depois de clonar este repositório, faça:

    $ virtualenv env;
    $ source env/bin/activate;
    $ pip install -r requirements.pip
    $ python manage.py migrate;

Este comando adiciona um superusuario na ferramenta:

    $ python manage.py createsuperuser;

Para rodar o serviço faça:

    $ python manage.py runserver;


