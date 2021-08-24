from controles import printaBarra, selecionaOpcao, adicionar, buscar, deletarContato, atualizar

size = 30

printaBarra(size)
print('\nIniciando Agenda\n')
printaBarra(size)

contatos = []  # type: list

while True:
    option = selecionaOpcao()
    print('~'*30)

    if option == '1':
        nome = input('Digite o nome: ')
        telefone = int(input('Digite o telefone: '))
        email = input('Digite o email: ')
        twitter = input('Digite o twitter: ')
        instagram = input('Digite o instagram: ')
        cntact = adicionar(nome, telefone, email, twitter, instagram)
        contatos.append(cntact)
        print('\nContato adicionado')
        printaBarra(size)

    elif option == '2':
        nome = input('Digite o nome do contato: ')
        print()
        buscar(contatos, nome)
        printaBarra(size)

    elif option == '3':
        nome = input('Digite o nome do contato a deletar: ')
        print()
        resultado = deletarContato(contatos, nome)
        printaBarra(size)

    elif option == '4':
        nome = input('Digite o nome do contato a atualizar: ')
        print()
        atualizar(contatos, nome)
        print('Contato atualizado!')
        printaBarra(size)

    elif option == '5':
        for contato in contatos:
            numero = contatos.index(contato) + 1
            print(numero)
            print(contato.getNome())
            print(contato.getTelefone())
            print(contato.getEmail())
            print(contato.getTwitter())
            print(contato.getInstagram())
            printaBarra(size)

    elif option == '6':
        break

    else:
        print('Opção inválida!')


print('\nEncerrando Agenda...')
printaBarra(size)
