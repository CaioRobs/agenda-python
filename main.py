import controles as controle


controle.printaBarra()
print('\nIniciando Agenda\n')
controle.printaBarra()

contatos = controle.ler()

while True:
    option = controle.selecionaOpcao()
    controle.printaBarra()

    if option == '1':
        nome = input('Digite o nome: ')
        telefone = int(input('Digite o telefone: '))
        email = input('Digite o email: ')
        twitter = input('Digite o twitter: ')
        instagram = input('Digite o instagram: ')
        contact = controle.adicionar(nome, telefone, email, twitter, instagram)
        contatos.append(contact)
        print('\nContato adicionado')
        controle.printaBarra()

    elif option == '2':
        nome = input('Digite o nome do contato: ')
        print()
        controle.buscar(contatos, nome)
        controle.printaBarra()

    elif option == '3':
        nome = input('Digite o nome do contato a deletar: ')
        print()
        resultado = controle.deletarContato(contatos, nome)
        controle.printaBarra()

    elif option == '4':
        nome = input('Digite o nome do contato a atualizar: ')
        print()
        controle.atualizar(contatos, nome)
        print('Contato atualizado!')
        controle.printaBarra()

    elif option == '5':
        for contato in contatos:
            numero = contatos.index(contato) + 1
            print(numero)
            print(contato.getNome())
            print(contato.getTelefone())
            print(contato.getEmail())
            print(contato.getTwitter())
            print(contato.getInstagram())
            controle.printaBarra()

    elif option == '6':
        controle.gravar(contatos)
        break

    else:
        print('Opção inválida!')

print('\nEncerrando Agenda...')
controle.printaBarra()
