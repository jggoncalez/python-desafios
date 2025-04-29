# Cadastro de animais domésticos

# Poder cadastrar
# Remover um cadastro
# Atualizar um cadastro
# Ver a lista de cadastro

db = []
id = 0

def menu():
    sel = int(input('''
                Seja bem-vindo ao cadastro de animais doméstimos
                1 - Cadastrar animais
                2 - Remover animais
                3 - Editar lista
                4 - Visualizar lista'''))
    options = {
        1: cadastrar,
        2: remover,
        3: editar,
        4: visualizar,
    }

def cadastrar():
    global id
    id += 1
    animal = input("Digite que animal você deseja cadastrar: ")
    raca = input("Digite a raça: ")
    idade = input("Digite a idade: ")
    peso = input("Digite o peso: ")

    db.append({
        "id": id,
        "animal": animal,
        "raca": raca,
        "idade": idade,
        "peso": peso
    })
    menu()

def remover():
    global id
    i = 0
    max = int(db.len)
    while i < max:
        print("\n".join([f"ID: {item['id']}, Animal: {item['animal']}, Raça: {item['raca']}, Idade: {item['idade']}, Peso: {item['peso']}" for item in db]))
        i += 1
    
    selRem = input('Digite a ID do animal que deseja remover: ')
    db.remove[selRem - 1]
    ans = input('Deseja retornar ao menu inicial? (y/n)')
    if (ans == 'y'):
        menu()
    else:
        pass


def editar():
    global id
    i = 0
    max = int(db.len)
    while i < max:
        print("\n".join([f"ID: {item['id']}, Animal: {item['animal']}, Raça: {item['raca']}, Idade: {item['idade']}, Peso: {item['peso']}" for item in db]))
        i += 1
    ans = input('Deseja retornar ao menu inicial? (y/n)')
    if (ans == 'y'):
        menu()
    else:
        pass
    


def visualizar():
    i = 0
    max = int(db.len)
    while i < max:
        print("\n".join([f"ID: {item['id']}, Animal: {item['animal']}, Raça: {item['raca']}, Idade: {item['idade']}, Peso: {item['peso']}" for item in db]))
        i += 1
    ans = input('Deseja retornar ao menu inicial? (y/n)')
    if (ans == 'y'):
        menu()
    else:
        pass

menu()