---
title: "Para que serve uma função? def e return na prática"
date: 2025-06-22
tag: aula03
reading_time: 4
featured: false
excerpt: Funções evitam repetição e tornam o código mais organizado. Entenda como criar as suas com def e return, e por que isso muda tudo.
---

# Funções: código que você escreve uma vez e usa várias

Imagina que você precisa calcular a média de um aluno em três partes diferentes do seu programa. Sem funções, você copiaria a mesma conta três vezes. Com funções, você escreve uma vez e **reutiliza**.

## Criando uma função com `def`

```python
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao Byte a Byte."
```

- `def` declara a função
- `saudacao` é o nome que você escolheu
- `nome` é o **parâmetro** — uma variável que recebe o valor quando a função é chamada
- `return` define o valor que a função devolve

## Chamando a função

```python
mensagem = saudacao("Ana")
print(mensagem)  # Olá, Ana! Bem-vindo ao Byte a Byte.

print(saudacao("Bruno"))  # Olá, Bruno! Bem-vindo ao Byte a Byte.
```

Você chama a função pelo nome e passa os **argumentos** entre parênteses.

## Funções com múltiplos parâmetros

```python
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

resultado = calcular_media(8.0, 7.5, 9.0)
print(f"Média: {resultado:.1f}")  # Média: 8.2
```

## Funções sem `return`

Nem toda função precisa devolver um valor. Algumas apenas executam uma ação:

```python
def exibir_aprovacao(nome, media):
    if media >= 7:
        print(f"{nome}: Aprovado! (média {media:.1f})")
    else:
        print(f"{nome}: Reprovado. (média {media:.1f})")

exibir_aprovacao("Carla", 8.5)  # Carla: Aprovado! (média 8.5)
exibir_aprovacao("Diego", 5.0)  # Diego: Reprovado. (média 5.0)
```

## Por que usar funções?

1. **Evitam repetição** — escreva a lógica uma vez
2. **Organizam o código** — cada função faz uma coisa só
3. **Facilitam a correção** — um bug? Corrija em um lugar só
4. **Tornam o código legível** — nomes de funções comunicam intenção

## Exemplo completo

```python
def aprovado(media):
    return media >= 7

def situacao(nome, notas):
    media = sum(notas) / len(notas)
    status = "Aprovado" if aprovado(media) else "Reprovado"
    print(f"{nome}: {status} (média {media:.1f})")

situacao("Ana",   [8.0, 9.0, 7.5])  # Ana: Aprovado (média 8.2)
situacao("Bruno", [4.0, 5.5, 6.0])  # Bruno: Reprovado (média 5.2)
```

Combinando funções com listas — o tema da nossa próxima leitura —, você consegue resolver problemas bem mais complexos.
