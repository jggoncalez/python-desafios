# Cadastro de animais domésticos

# Variáveis
db = [] # Simulação de banco de dados
id = 0 # ID para cada item no db

# Menu principal com escolhas
def menu():
    sel = int(input('''
Seja bem-vindo ao cadastro de animais domésticos
1 - Cadastrar animais
2 - Remover animais
3 - Editar lista
4 - Visualizar lista
5 - Sair
Escolha uma opção: '''))
    
    options = { # Opções em forma de dicionário, para o programa interpretar o número inserido e chamar a função
        1: cadastrar,
        2: remover,
        3: editar,
        4: visualizar,
    }
    
    if sel in options:  # Caso o número digitado pelo usuário esteja presente no menu:
        options[sel]() # Chamar a devida função
    elif sel == 5:
        print("Saindo do programa...")
        exit() # Função para encerrar o programa
    else:
        print("Opção inválida. Tente novamente.") # Caso número digitado não esteja presente, retornar ao menu inicial
        menu()

# Cadastro de animais domésticos
def cadastrar():
    global id
    id += 1 # ID dada de forma sequencial
    animal = input("Digite que animal você deseja cadastrar: ")
    raca = input("Digite a raça: ")
    idade = input("Digite a idade: ")
    peso = input("Digite o peso: ")

    db.append({ #inserção no banco de dados
        "id": id,
        "animal": animal,
        "raca": raca,
        "idade": idade,
        "peso": peso
    })
    menu()

# Remover elemento do banco de dados
def remover():
    global id
    for item in db:  # Itera diretamente sobre os itens no banco de dados de forma resumida
        print(f'''
{item['id']}.
Animal: {item['animal']}
        ''')
    
    selRem = int(input('Digite a ID do animal que deseja remover: '))
    for item in db:
        if item['id'] == selRem:
            db.remove(item)
            print("Animal removido com sucesso!")
            break
    else:
        print("ID não encontrado.")
    
    ans = input('Deseja retornar ao menu inicial? (y/n): ')
    if ans.lower() == 'y':
        menu()
    else:
        exit()

# Editar banco de dados
def editar():
    i = 0
    max = int(len(db))
    for item in db:  # Itera diretamente sobre os itens no banco de dados de forma resumida
        print(f'''
{item['id']}.
Animal: {item['animal']}
        ''')

    ans = input ('Dê o ID que deseja alterar: ')
    for item in db:
        if item['id'] == int(ans): # Apresenta o elemento de forma completa
            print(f'''
    Animal: {item['animal']},
    Raça: {item['raca']},
    Idade: {item['idade']}, 
    Peso: {item['peso']}
            ''')
            item['animal'] = input("Digite o novo nome do animal: ")
            item['raca'] = input("Digite a nova raça: ")
            item['idade'] = input("Digite a nova idade: ")
            item['peso'] = input("Digite o novo peso: ")
            print("Cadastro atualizado com sucesso!")
            break
        else:
            print("ID não encontrado.")
        
    ans = input('Deseja retornar ao menu inicial? (y/n): ')
    if ans.lower() == 'y':
        menu()
    else:
        exit()

 # Visualizar o banco de dados de forma complet

def visualizar():
    for item in db:  # Itera diretamente sobre os itens no banco de dados
        print(f'''
{item['id']}.
Animal: {item['animal']},
Raça: {item['raca']},
Idade: {item['idade']}, 
Peso: {item['peso']}
        ''')
    ans = input('Deseja retornar ao menu inicial? (y/n): ')
    if ans.lower() == 'y':
        menu()
    else:
        exit()

# Iniciar o programa com o menu
menu()