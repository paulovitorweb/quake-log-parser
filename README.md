# Quake log parser

![Code coverage](./coverage.svg) ![Test workflow](https://github.com/paulovitorweb/quake-log-parser/actions/workflows/test.yml/badge.svg)

Um parser escrito em Python para os logs do jogo Quake 3 Arena que fornece um relatório de cada partida.

## Como funciona

A aplicação lê os logs do provider e analisa os eventos `InitGame` e `Kill` para extrair estatísticas da partida, quais sejam:

- Total de kills da partida
- Lista de jogadores
- Kills por jogador

### Observações importantes

O jogador `<world>` não é listado entre os jogadores.

Sempre que um jogador é morto por `<world>`, perde 1 kill.

O total de kills não é a soma de kills dos jogadores, e sim a contagem do total de eventos do tipo `Kill` na partida.

Por `jogador`, entende-se aquele envolvido no evento `Kill`, seja porque matou ou porque foi morto. Ou seja, um jogador que entrou na partida mas não esteve envolvido nesse tipo de evento não é listado entre os jogadores da partida.

## Como executar a aplicação

Há duas maneiras de executar a aplicação: construindo a imagem via Docker ou executando via Python na máquina.

### Docker

Construa a imagem a partir da fonte:

```
$ make docker-build
```

Execute a aplicação dentro do container:

```
$ make docker-run
```

Para acessar e interagir com a API, vá até 127.0.0.1:8000/docs.

### Executando na máquina

Para executar direto na máquina local, você vai precisar de:

- Python >= 3.11
- GNU Make

Crie e ative um ambiente virtual:

```
$ python -m venv venv
$ source venv/bin/activate
```

Atualize o pip e instale o poetry:

```
$ pip install --upgrade pip
$ pip install poetry
```

Instale as dependências do projeto:

```
$ make install
```

Por fim, execute a aplicação:

```
$ make run
```

Se tudo correu bem, você poderá acessar 127.0.0.1:8000/docs.

## Testes

Há três conjuntos de testes que podem ser encontrados na pasta `tests`. São eles:

- unitários: testam pequenas unidades de código, isolando-as de dependências externas (como a leitura do arquivo de logs);
- de integração: testam as integrações do sistema com dependências externas, como o arquivo de logs;
- end-to-end: testam a API, verificando se as chamadas aos endpoints têm o retorno esperado dentro de cada cenário.

Os testes podem ser executados com:

```
$ make test
```

Esse comando também tem como output o relatório de cobertura do código com `pytest-cov`, além de atualizar o `coverage.svg`.

## Lint

Para manter um padrão de escrita do código, é utilizado o `ruff` como linter.

Execute-o com:

```
$ make lint
```

## Asyncio

Esta aplicação implementa simultaneidade baseada em corrotina com `asyncio`. Isso significa que o código é executado de maneira concorrente, através do que se chama de multitarefa cooperativa. 

Na prática, a API consegue tratar mais de um requisição "ao mesmo tempo", mesmo utilizando apenas um worker. Com isso, conseguimos aproveitar de forma mais eficiente os recursos da máquina para operações baseadas em I/O, como é o caso da leitura de arquivos de log.

Para alcançar isso, é importante garantir que operações de I/O bloqueantes passem longe da aplicação. Por isso, ao contribuir com o projeto, certifique-se de usar bibliotecas que implementam operações de I/O não bloqueantes, como a `aiofiles` para leitura de arquivos, `httpx` ou `aiohttp` para clientes http, `fastapi` para servidores web, etc.

### Suíte de testes assíncronos

A suíte de testes assíncronos foi construída com:

- pytest
- pytest-mock: que oferece uma fixture com recursos de mock do módulo unittest do Python
- httpx: para um cliente de testes com suporte a requisições http assíncronas
- asgi-lifespan: para encapsular o app FastAPI dentro de um lifespan
- pytest-asyncio: para testar código assíncrono com pytest
