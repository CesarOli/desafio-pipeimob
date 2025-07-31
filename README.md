# API de Gerenciamento de Livros - Desafio Pipeimob

API RESTful para gerenciar um sistema de cadastro de livros, com persistência em banco de dados e containerização via Docker, conforme especificado no desafio técnico da Pipeimob.

---

## ✨ Funcionalidades Implementadas

- ✅ **CRUD Completo de Livros**: Implementação de todos os endpoints obrigatórios para gerenciar os livros.
  - `GET /api/v1/books`: Listar todos os livros.
  - `GET /api/v1/books/{id}`: Obter um livro por ID.
  - `POST /api/v1/books`: Criar um novo livro.
  - `PUT /api/v1/books/{id}`: Atualizar um livro existente.
  - `DELETE /api/v1/books/{id}`: Remover um livro.
- ✅ **Webhook**: Rota `POST /api/v1/webhook` que recebe um payload JSON e o redireciona para uma URL externa.
- ✅ **Script de Seed**: Script para popular o banco de dados com dados fictícios para facilitar os testes.
- 💎 **Arquitetura Limpa**: A lógica de negócio é separada da camada de API (Service Layer) para melhor organização e testabilidade, seguindo boas práticas de modularização.
- 💎 **Autenticação Básica**: As rotas de criação (`POST`) e deleção (`DELETE`) de livros são protegidas por autenticação HTTP Basic.
- 💎 **Testes Automatizados**: Suíte de testes completa com `pytest` para garantir a qualidade e o funcionamento da API, incluindo testes para as rotas protegidas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **FastAPI**
- **PostgreSQL**
- **Docker & Docker Compose**
- **SQLAlchemy** (ORM)
- **Pydantic** (Validação de dados)
- **Pytest** (Testes automatizados)
- **Faker** (Geração de dados fictícios)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Docker
- Docker Compose
- Git

### Passos para Execução
1. Clone o repositório:
   ```bash
   git clone [https://github.com/CesarOli/desafio-pipeimob.git](https://github.com/CesarOli/desafio-pipeimob.git)
   cd desafio-pipeimob

2. Crie seu arquivo de ambiente local a partir do exemplo:
    ```bash
    cp .env.example .env
Importante: Edite o arquivo .env e defina um valor para POSTGRES_PASSWORD.

3. Suba os containers com Docker Compose:
    ```bash
    docker compose up --build -d

4. A API estará disponível em http://localhost:8001. 
   A documentação interativa (Swagger UI) pode ser acessada em: http://localhost:8001/docs


## 🧪 Como Testar a Aplicação

1. Testes Automatizados (Pytest)
Para rodar a suíte de testes completa que valida todas as funcionalidades do CRUD e a segurança, execute o seguinte comando no seu terminal:
    ```bash
    docker compose exec app bash -c "PYTHONPATH=. pytest -v"

2.  Testes Manuais (Swagger UI)
Acesse a documentação interativa em http://localhost:8001/docs

Testando Endpoints Públicos (GET, PUT)

- Expanda as rotas GET /api/v1/books ou PUT /api/v1/books/{id}.
- Clique em "Try it out" e depois em "Execute".

Testando Endpoints Protegidos (POST, DELETE)
- Clique no botão "Authorize" no canto superior direito.
- Na janela que abrir, digite as seguintes credenciais e clique em "Authorize":

Username: admin

Password: 123456

- Feche a janela. O cadeado agora estará fechado, indicando que você está autenticado.

- Agora, você pode expandir as rotas POST /api/v1/books ou DELETE /api/v1/books/{id} para testá-las.


Testando o Webhook
- Vá para um serviço como o 

https://webhook.site/ e copie a sua URL única. 

- No Swagger, expanda a rota POST /api/v1/webhook.

- Cole a URL do webhook.site no campo external_url.

- No campo Request body, insira um JSON válido (ex: {"test": 123}).

- Clique em "Execute" e verifique a página do webhook.site para ver o payload recebido.

