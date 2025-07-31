API de Gerenciamento de Livros - Desafio Pipeimob
🎯 Objetivo
O projeto consiste na criação de uma API RESTful para gerenciar um sistema de cadastro de livros, com persistência em banco de dados e containerização via Docker.

✨ Funcionalidades
✅ 

CRUD Completo de Livros: Implementação de todos os endpoints obrigatórios para gerenciar os livros.


GET /api/v1/books: Listar todos os livros.


GET /api/v1/books/{id}: Obter um livro por ID.


POST /api/v1/books: Criar um novo livro.


PUT /api/v1/books/{id}: Atualizar um livro existente.


DELETE /api/v1/books/{id}: Remover um livro.

✅ 

Webhook: Rota POST /api/v1/webhook que recebe um payload JSON e o redireciona para uma URL externa.

✅ 

Script de Seed: Script para popular o banco de dados com dados fictícios para facilitar os testes.

💎 

Arquitetura Limpa: A lógica de negócio é separada da camada de API (Service Layer) para melhor organização e testabilidade, seguindo boas práticas de modularização.

💎 

Autenticação Básica: As rotas de criação (POST) e deleção (DELETE) de livros são protegidas por autenticação HTTP Basic.

💎 

Testes Automatizados: Suíte de testes completa com pytest para garantir a qualidade e o funcionamento da API, incluindo testes para as rotas protegidas.

🛠️ Tecnologias Utilizadas

Python 3.8+ 


FastAPI 


PostgreSQL 


Docker & Docker Compose 

SQLAlchemy (ORM)

Pydantic (Validação de dados)


Pytest (Testes automatizados) 


Faker (Geração de dados fictícios) 

🚀 Como Executar o Projeto
Pré-requisitos
Docker

Docker Compose

Git

Passos para Execução
Clone o repositório:

Bash

git clone https://github.com/CesarOli/desafio-pipeimob.git
cd desafio-pipeimob
Crie seu arquivo de ambiente local a partir do exemplo:

Bash

cp .env.example .env
Importante: Edite o arquivo .env e defina uma senha segura para POSTGRES_PASSWORD.

Suba os containers com Docker Compose:

Bash

docker compose up --build -d
A API estará disponível em http://localhost:8001. A documentação interativa (Swagger UI) pode ser acessada em:
http://localhost:8001/docs

🧪 Como Testar a Aplicação
Existem duas formas de testar a aplicação:

1. Testes Automatizados (Pytest)
Para rodar a suíte de testes completa que valida todas as funcionalidades do CRUD e a segurança, execute o seguinte comando no seu terminal:

Bash

docker compose exec app bash -c "PYTHONPATH=. pytest -v"
2. Testes Manuais (Swagger UI)
Acesse a documentação interativa em http://localhost:8001/docs.

Testando Endpoints Públicos (GET, PUT)
Expanda as rotas GET /api/v1/books ou PUT /api/v1/books/{id}.

Clique em "Try it out" e depois em "Execute".

Testando Endpoints Protegidos (POST, DELETE)
As rotas de criação e deleção exigem autenticação.

Clique no botão "Authorize" no canto superior direito.

Na janela que abrir, digite as seguintes credenciais e clique em "Authorize":

Username: admin

Password: password123

Feche a janela. O cadeado agora estará fechado, indicando que você está autenticado.

Agora, você pode expandir as rotas POST /api/v1/books ou DELETE /api/v1/books/{id}, clicar em "Try it out" e "Execute" para testá-las.

Para testar o acesso negado, clique em "Authorize" novamente e depois em "Logout" antes de tentar executar uma rota protegida.

Testando o Webhook
Vá para um serviço de webhook, como o https://webhook.site/, e copie a sua URL única.

No Swagger, expanda a rota POST /api/v1/webhook.

Clique em "Try it out" e cole a URL do webhook.site no campo external_url.

No campo Request body, insira qualquer JSON válido (ex: {"test": 123}).

Clique em "Execute" e verifique a página do webhook.site para ver o payload recebido.
