---
title: "if, elif e else: tomando decisões com Python"
date: 2025-06-08
tag: aula02
reading_time: 4
featured: false
excerpt: Como ensinar o computador a escolher caminhos diferentes dependendo de uma condição. O bloco if/elif/else é a base de toda lógica de decisão.
preview: |
  if nota >= 7:
    print("Aprovado!")
  elif nota >= 5:
    print("Recuperação")
  else:
    print("Reprovado")
---

# Tomando decisões com `if`, `elif` e `else`

Todo programa precisa tomar decisões. "Se a nota for maior que 7, o aluno está aprovado. Se não, está reprovado." Esse tipo de lógica é implementada com **condicionais**.

## A estrutura básica: `if` e `else`

```python
nota = 8.5

if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado.")
```

Leia assim: **se** a nota for maior ou igual a 7, imprime "Aprovado!". **Senão**, imprime "Reprovado."

> A indentação (o espaço antes do `print`) não é opcional em Python — ela define o que pertence a cada bloco.

## Adicionando mais condições: `elif`

E se quisermos tratar o caso de recuperação?

```python
nota = 6.0

if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado.")
```

`elif` é uma abreviação de "else if" — uma condição adicional verificada só se a anterior for falsa.

## Operadores de comparação

Para construir condições, usamos:

| Operador | Significado       | Exemplo         |
|----------|-------------------|-----------------|
| `==`     | igual a           | `nota == 10`    |
| `!=`     | diferente de      | `cidade != "SP"`|
| `>`      | maior que         | `idade > 18`    |
| `<`      | menor que         | `preco < 50`    |
| `>=`     | maior ou igual    | `nota >= 7`     |
| `<=`     | menor ou igual    | `altura <= 2.0` |

## Combinando condições com `and` e `or`

```python
idade = 20
tem_ingresso = True

if idade >= 18 and tem_ingresso:
    print("Pode entrar!")
else:
    print("Entrada negada.")
```

- `and`: as **duas** condições precisam ser verdadeiras
- `or`: **pelo menos uma** das condições precisa ser verdadeira

## Exemplo completo

```python
temperatura = 28
chovendo = False

if temperatura > 30 and not chovendo:
    print("Perfeito para a praia!")
elif chovendo:
    print("Leve um guarda-chuva.")
else:
    print("Tempo agradável.")
```

Na próxima aula, veremos como fazer o computador **repetir** tarefas com `for` e `while`.
