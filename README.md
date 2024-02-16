# Flask Live Crud

Este projeto é uma aplicação CRUD (Create, Read, Update, Delete) construída com Flask, utilizando PostgreSQL como banco de dados e Docker para facilitar o desenvolvimento e o deployment.

## Pré-Requisitos

Antes de começar, você deve ter o Docker e o Docker Compose instalados em seu sistema. Visite [Docker](https://www.docker.com/get-started) para instruções de instalação.

## Configuração

Clone o repositório para a sua máquina local (ou faça o download dos arquivos) e navegue para o diretório do projeto.

```bash
git clone https://github.com/Vicrrs/flask_live_crud.git
cd flask_live_crud
```

## Como Usar

Dentro do diretório do projeto, execute os seguintes comandos para construir e iniciar sua aplicação e o banco de dados usando `docker-compose`.

### Construir e Iniciar a Aplicação

Para construir a imagem Docker do seu projeto e iniciar os serviços definidos no `docker-compose.yml` (sua aplicação Flask e o serviço PostgreSQL), execute:

```bash
docker-compose up --build
```

Esse comando irá automaticamente construir a imagem Docker da sua aplicação (se ainda não estiver construída) e iniciar os containers necessários. Se você preferir rodar os containers em background, adicione a flag `-d` ao comando:

```bash
docker-compose up --build -d
```

### Verificar os Containers em Execução

Para verificar os containers atualmente em execução, você pode usar o comando:

```bash
docker ps
```

### Acessar a Aplicação

Após os containers estarem em execução, sua aplicação estará acessível através do navegador ou de um cliente HTTP no endereço `http://localhost:5000`.

### Parar a Aplicação

Para parar os containers (e, opcionalmente, remover os containers, redes e volumes associados), você pode usar um dos seguintes comandos:

Para apenas parar os serviços:

```bash
docker-compose stop
```

Para parar e remover tudo (containers, redes criadas pelo `docker-compose up` e os volumes nomeados):

```bash
docker-compose down -v
```

## Manutenção do Banco de Dados

Para executar comandos de manutenção ou interagir diretamente com o banco de dados PostgreSQL, você pode usar o seguinte comando para acessar o shell do container do banco de dados:

```bash
docker-compose exec flask_db psql -U postgres
```

Substitua `postgres` pelo nome de usuário que você configurou para o banco de dados, se diferente.

## Feedback

Para reportar bugs ou solicitar novas funcionalidades, sinta-se à vontade para abrir uma issue no repositório do GitHub.


