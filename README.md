# API Python

## API criada em Python para aprendizado


Como CRIAR uma API com PYTHON do Dev Aprender

Link do video: https://www.youtube.com/watch?v=FBLAV1SbJFk

Sobre API: É um lugar para disponibilizar recursos e/ou funcionalidades.

Para se criar uma API a de se pensar em 4 etapas principais, sendo elas:

- 1 - Objetivo

- 2 - URL base

- 3 - Endpoints

- 4 - Quais recursos iremos disponibilizar


## Objetivo:
```
Criar uma API que disponibiliza a consulta, criação, edição e exclusão de livros.
```

## URL base

```
É o local para o qual sera feito a requisição, nesse caso sera o localhost
```

## Endpoints

```
Os endpoints são endereços onde as funcionalidades serão disponibilizadas na API, no caso dessa API:
    - localhost/livros (GET)
    - localhost/livros (POST)
    - localhost/livros/id (GET)
    - localhost/livros/id (PUT)
    - localhost/livros/id (DELETE)
```

## Pacotes utilizado

```
    pip install Flask
```