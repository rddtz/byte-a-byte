---
title: "Listas em Python: guardando vários valores de uma vez"
date: 2025-06-22
tag: aula03
reading_time: 4
featured: false
excerpt: Uma lista é como uma caixa que guarda vários itens em ordem. Aprenda a criar, acessar, modificar e percorrer listas — um dos recursos mais usados em Python.
---

# Listas: guardando vários valores de uma vez

Até agora, cada variável guardava um único valor. Mas e se você precisar guardar as notas de 30 alunos? Criar 30 variáveis seria impraticável.

A solução é a **lista**.

## Criando uma lista

```python
frutas = ["maçã", "banana", "uva", "manga"]
notas  = [8.5, 7.0, 9.5, 6.0]
mista  = ["Ana", 21, True, 9.5]  # listas podem misturar tipos
```

Listas usam colchetes `[]` e separam os itens com vírgulas.

## Acessando itens pelo índice

Cada item tem uma posição — chamamos de **índice**, começando em `0`:

```python
frutas = ["maçã", "banana", "uva"]

print(frutas[0])   # maçã   (primeiro)
print(frutas[1])   # banana (segundo)
print(frutas[-1])  # uva    (último, índice negativo)
```

## Modificando a lista

```python
frutas = ["maçã", "banana", "uva"]

frutas.append("manga")    # adiciona no final
frutas.insert(1, "kiwi")  # insere na posição 1
frutas.remove("banana")   # remove pelo valor
frutas.pop()              # remove e retorna o último item

print(len(frutas))  # len() retorna o tamanho da lista
```

## Percorrendo uma lista com `for`

```python
alunos = ["Ana", "Bruno", "Carla"]

for aluno in alunos:
    print(f"Olá, {aluno}!")
```

Para percorrer com índice:

```python
for i, aluno in enumerate(alunos):
    print(f"{i + 1}. {aluno}")
```

## Operações úteis

```python
notas = [8.5, 7.0, 9.5, 6.0, 8.0]

print(sum(notas))   # 39.0  — soma
print(max(notas))   # 9.5   — maior valor
print(min(notas))   # 6.0   — menor valor
print(len(notas))   # 5     — quantidade de itens

media = sum(notas) / len(notas)
print(f"Média da turma: {media:.1f}")  # Média da turma: 7.8
```

## Fatiamento (slicing)

```python
numeros = [0, 1, 2, 3, 4, 5]

print(numeros[1:4])   # [1, 2, 3]  — do índice 1 ao 3
print(numeros[:3])    # [0, 1, 2]  — do início ao índice 2
print(numeros[3:])    # [3, 4, 5]  — do índice 3 ao fim
```

## Exemplo completo

```python
def aprovados(notas):
    return [nota for nota in notas if nota >= 7]

turma = [8.5, 5.0, 9.0, 6.5, 7.5, 4.0, 8.0]
passou = aprovados(turma)

print(f"Total: {len(turma)} alunos")
print(f"Aprovados: {len(passou)}")
print(f"Média dos aprovados: {sum(passou)/len(passou):.1f}")
```

Listas são a base de muitas estruturas de dados em Python — dominá-las abre a porta para problemas muito mais interessantes.
