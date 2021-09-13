# Fastapi-Nano com Docker utilizando Poetry

Este projeto foi baseado no Fastapi-Nano. Porém, fiz ajustes
para poder rodá-lo utilizando Docker e Poetry. 

Também foram acrescentado o Dynaconf para leitura de arquivos de configuração 
e o Loguru (excelente logger).

A parte do Docker foi baseada no projeto https://github.com/marcelopalin/python-poetry-docker-example


# Baixei o projeto do Git, e agora?

Primeiro, você deve ter instalado em sua máquina o Poetry e o Docker.
Existem muitos tutoriais na internet que ensinam como instalá-los. 

Uma vez instalados para executar a API manualmente (sem o Docker) faça:

```s
poetry install
```

Rode com:

```s
poetry shell
```
```s
uvicorn app.main:app --reload --host localhost --port 5000
```

ou sem ativar o ambiente:

```s
poetry run uvicorn app.main:app --reload --host localhost --port 5000
```


## Construindo Imagem do Container

Digite este comando na raiz do projeto:

```s
docker build --tag fastapi-nano-palin  . 
```

Irá construir a Imagem `fastapi-nano-palin`

Para executar a Imagem como teste fça

```s
docker run -d -p 5000:8000 --rm fastapi-nano-palin:latest
```

Acesse http://localhost:5000/docs#/

<div align="center">
<i> ✨ 🍰 ✨ </i>
</div>

