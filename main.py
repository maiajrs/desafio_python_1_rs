def add_contato(contato): 
    contatos.append(contato)
    return
def ver_todos_contatos():
    if len(contatos) == 0:
        print("\nAinda não existem contatos cadastrados.")
        return
    print("\nAqui estão todos os seus contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito_existe = contato.get('favorito', None)
        favorito = '[*]' if favorito_existe else "[ ]"
        print(f"\nID: {indice} | Nome: {contato['nome']} | Telefone: {contato['telefone']} | Email: {contato['email']} | Favorito: {favorito}")
    return
def find_by_id(id):
    for indice, contato in enumerate(contatos, start=1):
        if indice == id:
            return contato
    return None

def ver_todos_contatos_favoritos():
    print("\nAqui estão todos os seus contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito_existe = contato.get('favorito', None)
        if favorito_existe:
            print(f"\nID: {indice} | Nome: {contato['nome']} | Telefone: {contato['telefone']} | Email: {contato['email']} | Favorito: [*]")
    return

contatos = []

while True: 
    print("\nBem-vindo a sua agenda online!")
    print("\nSelecione umas das opções do menu:")
    print("\n1 - Para adicionar um novo contato.")
    print("\n2 - Para visualizar seus contatos.")
    print("\n3 - Para editar um contato.")
    print("\n4 - Para marcar um contato como favorito.")
    print("\n5 - Para desmarcar um contato como favorito.")
    print("\n6 - Para ver seus contatos favoritos.")
    print("\n7 - Para apagar um contato.")
    
    opcao = None
    try: 
        opcao = int(input("\nDigite uma opcão: "))
    except KeyboardInterrupt:
        print("\nAté logo!!")
        exit()
    except Exception as e:
        print("\nOpção inválida!")
        print("\nDigite um número inteiro como opção.")
        continue
    if opcao == 1:
        nome = input("\nDigite o nome do contato: ")
        telefone = input("\nDigite o telefone do contato: ")
        email = input("\nDigite o email do contato: ")
        contato = {"nome": nome, "telefone": telefone, "email": email}

        add_contato(contato)
    elif opcao == 2:
        ver_todos_contatos()
    elif opcao == 3:

        id = None

        ver_todos_contatos()

        while id == None:
            try: 
                id = int(input("\nDigite o numero do contato a ser editado: "))
            except:
                print("\nOpção inválida!")
                print("\nDigite um número inteiro como opção.")
                continue

        contato = find_by_id(id)

        print("Este é o contato a ser atualizado: ")
        favorito_existe = contato.get('favorito', None)
        favorito = ' | [*]' if favorito_existe else ""
        print(f"\nNome: {contato['nome']} | Telefone: {contato['telefone']} | Email: {contato['email']} {favorito}")

        nome = None
        telefone = None
        email = None

        print("Deseja alterar o nome?")
        nomeS = input("Tecle s para SIM ou n para NÃO: ")
        if (nomeS.lower() == 's'): 
            nome = input("\nDigite o novo nome do contato: ")
            contato['nome'] = nome
        
        print("Deseja alterar o telefone?")
        telefoneS = input("Tecle s para SIM ou n para NÃO: ")
        if (telefoneS.lower() == 's'): 
            telefone = input("\nDigite o novo telefone do contato: ")
            contato['telefone'] = telefone
        
        print("Deseja alterar o email?")
        emailS = input("Tecle s para SIM ou n para NÃO: ")
        if (emailS.lower() == 's'): 
            email = input("\nDigite o novo email do contato: ")
            contato['email'] = email
    elif opcao == 4: 
        ver_todos_contatos()
        id = None
        while id == None:
            try: 
                id = int(input("\nDigite o numero do contato a ser favoritado: "))
            except:
                print("\nOpção inválida!")
                print("\nDigite um número inteiro como opção.")
                continue

        contato = find_by_id(id)

        if (contato): 
            contato['favorito'] = True
            print("\nContato favoritado com sucesso!")
        else:
            print("\nContato não encontrado!")
    elif opcao == 5:
        ver_todos_contatos()
        id = None
        while id == None:
            try: 
                id = int(input("\nDigite o numero do contato a ser desmarcado como favorito: "))
            except:
                print("\nOpção inválida!")
                print("\nDigite um número inteiro como opção.")
                continue

        contato = find_by_id(id)

        if (contato): 
            contato['favorito'] = False
            print("\nContato desmarcado como favorito com sucesso!")
        else:
            print("\nContato não encontrado!")
    elif opcao == 6:
        ver_todos_contatos_favoritos()
    elif opcao == 7:
        ver_todos_contatos()
        id = None
        while id == None:
            try: 
                id = int(input("\nDigite o numero do contato a ser apagado: "))
            except:
                print("\nOpção inválida!")
                print("\nDigite um número inteiro como opção.")
                continue

        contato = find_by_id(id)

        if (contato): 
            contatos.remove(contato)
            print("\nContato apagado com sucesso!")
        else:
            print("\nContato não encontrado!")
    else:
        print("\nVocê não selecionou uma opção válida!")
