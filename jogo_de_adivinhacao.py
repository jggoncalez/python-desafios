import random

baralho = ["a", "k", "q", "j", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
nomes = {
    "a": "Ás",
    "k": "Rei",
    "q": "Rainha",
    "j": "Valete"
}

while True:
    cartas = baralho.copy()
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
            cartas = baralho.copy()
            cartasEsc = []
            i = 0

    # Jogador escolhe uma carta
    escolha = input(f'\nEscolha uma carta:\n{cartasEsc}\n').lower().strip()

    # Função de adivinhação (cole aqui sua versão corrigida com slices)
    def adivinhacao():
        global resp
        ans = input("Sua carta é uma figura (Ás, Rei, Rainha ou Valete)? (y/n) ").lower()
        if ans == "y":
            resp = resp[:4]
            ans = input("Sua carta é da alta nobreza (Rei ou Rainha)? (y/n) ").lower()
            if ans == "y":
                resp = resp[1:3]
                ans = input("Sua carta representa uma personagem feminina (Rainha)? (y/n) ").lower()
                if ans == "y":
                    resp = [resp[1]]
                    return
                else:
                    resp = [resp[0]]
                    return
            else:
                resp = [resp[0], resp[3]]
                ans = input("Sua carta representa um personagem (Valete)? (y/n) ").lower()
                if ans == "y":
                    resp = [resp[1]]
                    return
                else:
                    resp = [resp[0]]
                    return
        else:
            resp = resp[4:]
            ans = input("Sua carta é um número par (2, 4, 6, 8, 10)? (y/n) ").lower()
            if ans == "y":
                resp = resp[::2]
                ans = input("Sua carta é menor que 5 (2 ou 4)? (y/n) ").lower()
                if ans == "y":
                    resp = resp[-2:]
                    ans = input("Sua carta é a mais baixa (2)? (y/n) ").lower()
                    if ans == "y":
                        resp = [resp[1]]
                        return
                    else:
                        resp = [resp[0]]
                        return
                else:
                    resp = resp[:3]
                    ans = input("Sua carta é a maior entre elas (10)? (y/n) ").lower()
                    if ans == "y":
                        resp = [resp[0]]
                        return
                    else:
                        resp = resp[1:]
                        ans = input("Sua carta é múltipla de 3 (6)? (y/n) ").lower()
                        if ans == "y":
                            resp = [resp[1]]
                            return
                        else:
                            resp = [resp[0]]
                            return
            else:
                resp = resp[1::2]
                ans = input("Sua carta é um número primo (3 ou 7)? (y/n) ").lower()
                if ans == "n":
                    resp = [resp[0], resp[2]]
                    ans = input("Sua carta é 5? (y/n) ").lower()
                    if ans == "y":
                        resp = [resp[1]]
                    else:
                        resp = [resp[0]]
                    return
                else:
                    resp = resp[1:3]
                    ans = input("Sua carta é múltipla de 3 (3)? (y/n) ").lower()
                    if ans == "y":
                        resp = [resp[1]]
                        return
                    else:
                        resp = [resp[0]]
                        return

    # Executa a adivinhação
    adivinhacao()

    # Resultado
    resp = resp[0]
    if resp == escolha:
        resultado = "certo"
    else:
        resultado = "errado... oh não"

    print(f'Sua carta é {nomes.get(resp, resp)}. Ou seja, estou {resultado}.')

    # Pergunta se quer jogar de novo
    jogar_novamente = input("\nQuer jogar novamente? (y/n): ").lower()
    if jogar_novamente != "y":
        print("Até a próxima!")
        break