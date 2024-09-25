<h1>Flask API com MongoDB e Docker</h1>

<p>Este projeto é uma API construída com Flask que utiliza um banco de dados MongoDB e é executada dentro de containers Docker. A API permite gerenciar músicas e piadas, retornando dados aleatórios ou específicos conforme solicitado.</p>

<h2>Funcionalidades</h2>
<ul>
    <li><strong>Músicas:</strong>
        <ul>
            <li>Criar uma nova música.</li>
            <li>Retornar todas as músicas.</li>
            <li>Retornar uma música específica por ID.</li>
            <li>Retornar uma música aleatória.</li>
        </ul>
    </li>
    <li><strong>Piadas:</strong>
        <ul>
            <li>Criar uma nova piada.</li>
            <li>Retornar todas as piadas.</li>
            <li>Retornar uma piada específica por ID.</li>
            <li>Retornar uma piada aleatória.</li>
        </ul>
    </li>
</ul>

<h2>Tecnologias Utilizadas</h2>
<ul>
    <li><strong>Python:</strong> Linguagem principal usada para construir a API.</li>
    <li><strong>Flask:</strong> Framework web usado para criar os endpoints da API.</li>
    <li><strong>MongoDB:</strong> Banco de dados NoSQL usado para armazenar as músicas e piadas.</li>
    <li><strong>Docker:</strong> Usado para containerizar a aplicação.</li>
    <li><strong>Waitress:</strong> Servidor WSGI para executar a aplicação em produção.</li>
</ul>

<h2>Estrutura do Projeto</h2>
<pre>
/src
│
├── app.py                 # Arquivo principal para iniciar o servidor Flask
├── controllers             # Controladores para gerenciar as rotas da API
│   ├── musics_controller.py
│   └── jokes_controller.py
├── models                  # Modelos que interagem com o MongoDB
│   ├── music_model.py
│   └── joke_model.py
├── db.py                   # Configuração da conexão com o MongoDB
├── abstract_model.py        # Classe abstrata para as operações comuns entre os modelos
├── requirements.txt         # Dependências do projeto
└── dev-requirements.txt     # Dependências de desenvolvimento
</pre>

<h2>Endpoints</h2>

<h3>Músicas</h3>
<ul>
    <li><strong>POST</strong> <code>/musics</code> — Adiciona uma nova música.</li>
    <li><strong>GET</strong> <code>/musics</code> — Retorna todas as músicas.</li>
    <li><strong>GET</strong> <code>/musics/random</code> — Retorna uma música aleatória.</li>
    <li><strong>GET</strong> <code>/musics/&lt;id&gt;</code> — Retorna uma música específica pelo ID.</li>
</ul>

<h3>Piadas</h3>
<ul>
    <li><strong>POST</strong> <code>/jokes</code> — Adiciona uma nova piada.</li>
    <li><strong>GET</strong> <code>/jokes</code> — Retorna todas as piadas.</li>
    <li><strong>GET</strong> <code>/jokes/random</code> — Retorna uma piada aleatória.</li>
    <li><strong>GET</strong> <code>/jokes/&lt;id&gt;</code> — Retorna uma piada específica pelo ID.</li>
</ul>

<h2>Como Executar o Projeto</h2>

<h3>Usando Docker</h3>
<ol>
    <li>Certifique-se de ter o Docker instalado.</li>
    <li>No diretório raiz do projeto, execute o comando abaixo para iniciar a API e o MongoDB:
        <pre><code>docker-compose up --build</code></pre>
    </li>
    <li>Acesse a API em <a href="http://localhost:8000">http://localhost:8000</a>.</li>
</ol>

<h3>Sem Docker</h3>
<ol>
    <li>Instale as dependências:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Configure a URL do MongoDB (pode ser um MongoDB local):
        <pre><code>export MONGO_URL=mongodb://localhost:27017</code></pre>
    </li>
    <li>Execute a aplicação:
        <pre><code>python app.py</code></pre>
    </li>
    <li>A aplicação estará disponível em <a href="http://localhost:8000">http://localhost:8000</a>.</li>
</ol>

<h2>Variáveis de Ambiente</h2>
<ul>
    <li><strong>MONGO_URL:</strong> URL de conexão ao MongoDB.</li>
    <li><strong>FLASK_ENV:</strong> Define o ambiente da aplicação (<code>dev</code> para desenvolvimento).</li>
</ul>

<h2>Docker</h2>
<p>O projeto possui um <code>Dockerfile</code> e um <code>docker-compose.yml</code> que criam containers tanto para a aplicação Flask quanto para o MongoDB.</p>

<ul>
    <li><strong>Dockerfile:</strong> Define a imagem do container para a API Flask.</li>
    <li><strong>docker-compose.yml:</strong> Orquestra os containers da API e do MongoDB.</li>
</ul>

<h3>Comandos Úteis</h3>
<ul>
    <li>Subir os containers:
        <pre><code>docker-compose up --build</code></pre>
    </li>
    <li>Derrubar os containers:
        <pre><code>docker-compose down</code></pre>
    </li>
</ul>

<h2>Autor</h2>
<p>Este projeto foi desenvolvido por Wladyr durante curso da trybe.</p>
