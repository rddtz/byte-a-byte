---
title: "for e while: quando o computador precisa repetir"
date: 2025-06-15
tag: aula02
reading_time: 5
featured: false
excerpt: Laços de repetição são uma das ferramentas mais poderosas da programação. Veja como e quando usar cada um — e como não cair em loops infinitos.
---

# Laços de repetição: `for` e `while`

Imagine que você precisa imprimir "Olá!" 100 vezes. Escrever `print("Olá!")` cem vezes não é a resposta. A resposta são os **laços de repetição**.

## O laço `for`

O `for` é ideal quando você sabe **quantas vezes** quer repetir algo, ou quando quer percorrer uma sequência:

```python
for i in range(5):
    print(f"Vez {i + 1}")
```

Saída:
```
Vez 1
Vez 2
Vez 3
Vez 4
Vez 5
```

### Entendendo o `range()`

- `range(5)` gera os números de `0` a `4` (5 não está incluído)
- `range(1, 6)` gera de `1` a `5`
- `range(0, 10, 2)` gera `0, 2, 4, 6, 8` (passo de 2)

## O laço `while`

O `while` repete enquanto uma condição for verdadeira — útil quando não sabemos de antemão quantas repetições serão necessárias:

```python
tentativas = 0

while tentativas < 3:
    print(f"Tentativa {tentativas + 1}")
    tentativas += 1

print("Fim das tentativas.")
```

> **Cuidado com loops infinitos!** Se a condição nunca se tornar falsa, o programa nunca para. Certifique-se de que a variável que controla o `while` é atualizada a cada iteração.

## `for` vs `while`: quando usar cada um?

| Situação                              | Use       |
|---------------------------------------|-----------|
| Sabe quantas repetições serão feitas  | `for`     |
| Percorrer uma lista ou sequência      | `for`     |
| Repetir até uma condição mudar        | `while`   |
| Aguardar uma entrada do usuário       | `while`   |

## Percorrendo uma lista com `for`

```python
nomes = ["Ana", "Bruno", "Carla"]

for nome in nomes:
    print(f"Olá, {nome}!")
```

Saída:
```
Olá, Ana!
Olá, Bruno!
Olá, Carla!
```

## Controlando o laço: `break` e `continue`

```python
for numero in range(10):
    if numero == 5:
        break  # para o laço completamente
    if numero % 2 == 0:
        continue  # pula para a próxima iteração
    print(numero)
```

Saída: `1  3` (números ímpares menores que 5)

## Exemplo prático

```python
soma = 0

for numero in range(1, 11):
    soma += numero

print(f"Soma de 1 a 10: {soma}")  # Soma de 1 a 10: 55
```

Na próxima aula vamos organizar dados em **listas** e criar blocos de código reutilizáveis com **funções**.
