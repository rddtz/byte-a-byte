---
title: O que são tipos de dados? int, float, str e bool explicados
date: 2025-06-01
tag: aula01
reading_time: 5
featured: true
excerpt: Antes de escrever qualquer programa, você precisa entender como o Python representa a informação. Exploramos os quatro tipos básicos com exemplos do cotidiano.
preview: |
  nome = "Ana"        # str
  idade = 21          # int
  altura = 1.65       # float
  aprovada = True     # bool

  print(type(nome))   # <class 'str'>
---

# O que são tipos de dados?

Quando você escreve um programa, está manipulando informação. Mas o computador precisa saber **que tipo** de informação está lidando — um número inteiro é diferente de um texto, que é diferente de um valor verdadeiro ou falso.

É aí que entram os **tipos de dados**.

## Os quatro tipos básicos do Python

### `int` — Números inteiros

```python
idade = 21
ano = 2025
quantidade = 100
```

Use `int` para quantidades sem parte decimal: idade, contagem, ano.

### `float` — Números decimais

```python
altura = 1.75
temperatura = 36.6
preco = 9.99
```

Quando precisar de casas decimais, use `float`. O ponto (`.`) separa a parte inteira da decimal — diferente da vírgula que usamos na escrita comum.

### `str` — Texto

```python
nome = "Ana"
cidade = 'Porto Alegre'
frase = "Olá, mundo!"
```

Textos sempre ficam entre aspas — simples ou duplas. Em Python, chamamos texto de **string** (abreviado como `str`).

### `bool` — Verdadeiro ou falso

```python
aprovada = True
chovendo = False
```

O tipo `bool` só tem dois valores possíveis: `True` ou `False`. É a base de toda lógica de decisão em um programa.

## Como descobrir o tipo de uma variável

O Python tem uma função chamada `type()` que revela o tipo de qualquer valor:

```python
nome = "Maria"
nota = 9.5
aprovada = True

print(type(nome))      # <class 'str'>
print(type(nota))      # <class 'float'>
print(type(aprovada))  # <class 'bool'>
```

## Misturando tipos: cuidado!

Python não mistura tipos automaticamente em certas operações:

```python
idade = 21
mensagem = "Você tem " + idade + " anos"  # TypeError!
```

Para juntar texto com número, você precisa converter explicitamente:

```python
# Opção 1: converter com str()
mensagem = "Você tem " + str(idade) + " anos"

# Opção 2: f-string (mais elegante)
mensagem = f"Você tem {idade} anos"
```

## Resumo

| Tipo    | Exemplo         | Quando usar             |
|---------|-----------------|-------------------------|
| `int`   | `21`, `100`     | Números inteiros        |
| `float` | `1.75`, `9.99`  | Números com decimal     |
| `str`   | `"Ana"`         | Textos                  |
| `bool`  | `True`, `False` | Verdadeiro ou falso     |

Na próxima aula, vamos usar esses tipos para tomar **decisões** com `if` e `else`.
