﻿# Flask API com MongoDB e Docker

 Este projeto é uma API construída com Flask que utiliza um banco de dados MongoDB e é executada dentro de containers Docker. A API permite gerenciar músicas e piadas, retornando dados aleatórios ou específicos conforme solicitado.

Funcionalidades
  Músicas:
    Criar uma nova música.
    Retornar todas as músicas.
    Retornar uma música específica por ID.
    Retornar uma música aleatória.

  Piadas:
    Criar uma nova piada.
    Retornar todas as piadas.
    Retornar uma piada específica por ID.
    Retornar uma piada aleatória.

Tecnologias Utilizadas
  Python: Linguagem principal usada para construir a API.
  Flask: Framework web usado para criar os endpoints da API.
  MongoDB: Banco de dados NoSQL usado para armazenar as músicas e piadas.
  Docker: Usado para containerizar a aplicação.
  Waitress: Servidor WSGI para executar a aplicação em produção.

Endpoints
  Músicas
    POST /musics — Adiciona uma nova música.
    GET /musics — Retorna todas as músicas.
    GET /musics/random — Retorna uma música aleatória.
    GET /musics/<id> — Retorna uma música específica pelo ID.

  Piadas
    POST /jokes — Adiciona uma nova piada.
    GET /jokes — Retorna todas as piadas.
    GET /jokes/random — Retorna uma piada aleatória.
    GET /jokes/<id> — Retorna uma piada específica pelo ID.


  Como Executar o Projeto
    Usando Docker
      Certifique-se de ter o Docker instalado.
      No diretório raiz do projeto, execute o comando abaixo para iniciar a API e o MongoDB:
        docker-compose up --build

    Sem Docker
      Instale as dependências:
        pip install -r requirements.txt
      Configure a URL do MongoDB (pode ser um MongoDB local):
        export MONGO_URL=mongodb://localhost:27017
      Execute a aplicação:
        python app.py
        
A aplicação estará disponível em http://localhost:8000.




 
