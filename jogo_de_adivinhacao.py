
import random

# Lista de cartas
cartas = ["a", "k", "q", "j", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
resp = cartas.copy()
cartasEsc = []
i = 0

# Escolhe 5 cartas aleatórias
while i < 5:
    try:
        a = random.choice(cartas)
        cartasEsc.append(a)
        cartas.remove(a)
        i += 1
    except ValueError:
        print("Erro ao selecionar carta. Tentando novamente...")
        cartas = ["a", "k", "q", "j", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        cartasEsc = []
        i = 0

# Jogador escolhe uma carta
escolha = input(f'Escolha uma carta:\n{cartasEsc}\n').lower().strip()

# Função de adivinhação
def adivinhacao():
    global resp
    ans = input("Sua carta é uma figura (Rei, Rainha, Valete, Ás)? (y/n) ").lower()
    if ans == "y":
        resp = resp[:4]  # Mantém figuras
        ans = input("Sua carta é da alta nobreza (Rei ou Rainha)? (y/n) ").lower()
        if ans == "y":
            resp = resp[:2]  # Rei e Rainha
            ans = input("Sua carta representa uma personagem feminina? (y/n) ").lower()
            if ans == "y":
                resp = [resp[1]]  # Rainha
            else:
                resp = [resp[0]]  # Rei
        else:
            resp = resp[2:]  # Valete e Ás
            ans = input("Sua carta representa um personagem? (y/n) ").lower()
            if ans == "y":
                resp = [resp[0]]  # Valete
            else:
                resp = [resp[1]]  # Ás
    else:
        resp = resp[4:]  # Numéricas
        ans = input("Sua carta é um número par? (y/n) ").lower()
        if ans == "y":
            resp = resp[::2]  # Pares
            ans = input("Sua carta é menor que 5? (y/n) ").lower()
            if ans == "y":
                resp = resp[:2]  # 2 e 4
                ans = input("Sua carta é a mais baixa (exceto Ás)? (y/n) ").lower()
                if ans == "y":
                    resp = [resp[0]]  # 2
                else:
                    resp = [resp[1]]  # 4
            else:
                resp = resp[2:]  # 6, 8, 10
                ans = input("Sua carta é a maior (exceto figuras)? (y/n) ").lower()
                if ans == "y":
                    resp = [resp[-1]]  # 10
                else:
                    resp.remove("10")  # Fica 6 ou 8
                    ans = input("Sua carta é múltipla de 3? (y/n) ").lower()
                    if ans == "y":
                        resp = [resp[0]]  # 6
                    else:
                        resp = [resp[1]]  # 8
        else:
            resp = resp[1::2]  # Ímpares
            ans = input("Sua carta é um número primo (3 ou 7)? (y/n) ").lower()
            if ans == "n":
                resp = [resp[0]]  # 9
            else:
                resp = resp[1:]  # 3 e 7
                ans = input("Sua carta é múltipla de 3? (y/n) ").lower()
                if ans == "y":
                    resp = [resp[0]]  # 3
                else:
                    resp = [resp[1]]  # 7

# Executa adivinhação
adivinhacao()

# Resultado
resp = resp[0]
if resp == escolha:
    resultado = "certo"
else:
    resultado = "errado... oh não"

# Tradução dos códigos de carta pelo metódo do dicionário
nomes = {
    "a": "Ás",
    "k": "Rei",
    "q": "Rainha",
    "j": "Valete"
}

# Imprime resultado
print(f'Sua carta é {nomes.get(resp, resp)}. Ou seja, estou {resultado}.')