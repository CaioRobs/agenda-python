import controles

printaBarra()
print('\nIniciando Agenda\n')
printaBarra()

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
        cntact = controles.adicionar(nome, telefone, email, twitter, instagram)
        contatos.append(cntact)
        print('\nContato adicionado')
        printaBarra()

    elif option == '2':
        nome = input('Digite o nome do contato: ')
        print()
        controles.buscar(contatos, nome)
        printaBarra()

    elif option == '3':
        nome = input('Digite o nome do contato a deletar: ')
        print()
        resultado = controles.deletarContato(contatos, nome)
        printaBarra()

    elif option == '4':
        nome = input('Digite o nome do contato a atualizar: ')
        print()
        controles.atualizar(contatos, nome)
        print('Contato atualizado!')
        printaBarra()

    elif option == '5':
        for contato in contatos:
            numero = contatos.index(contato) + 1
            print(numero)
            print(contato.getNome())
            print(contato.getTelefone())
            print(contato.getEmail())
            print(contato.getTwitter())
            print(contato.getInstagram())
            printaBarra()

    elif option == '6':
        break

    else:
        print('Opção inválida!')


print('\nEncerrando Agenda...')
printaBarra()
