# Biblioteca API

Este é um projeto de API para gerenciar uma biblioteca de livros.

## Configuração do Ambiente

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/thallyslemos/biblioteca-cepedi
    cd biblioteca-cepedi
    ````

2. **Crie um ambiente virtual com Python:**

    ```bash
    python3 -m venv .venv
    ````

3. **Ative o ambiente virtual:**

    ```bash
    # No Linux
    source .venv/bin/activate

    # No Windows
    .venv\Scripts\activate
    ````

4. **Instale as dependências:**

    ```bash
    python3 -m pip install -r requirements.txt
    ````

5. **Execute as migrações do banco de dados:**

    ```bash
    python3 manage.py migrate
    ````

6. **Inicie o servidor de desenvolvimento:**

    ```bash
    python3 manage.py runserver
    ````

7. **Acesse a API em `http://localhost:8000/`**

Operaçoes disponíveis:	
- GET /api/livros/ - Lista todos os livros
- POST /api/livros/ - Cria um novo livro
- GET /api/livros/{id}/ - Mostra detalhes de um livro
- PUT /api/livros/{id}/ - Atualiza um livro
- DELETE /api/livros/{id}/ - Deleta um livro

# Body para POST e PUT
```json
    {
        "id": 1,
        "titulo": "Titulo do Livro",
        "autor": 1, // ID do autor
        "categoria": 1, // ID da categoria
        "publicado_em": "1951-06-01"
    }
```
- Os múdulos de autor e categoria ainda não possuem operações de CRUD, então é necessário criar manualmente no banco de dados.

