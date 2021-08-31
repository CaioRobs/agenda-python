import json
from contato import Contato


def printaBarra():
    barra_size = 30
    print('~'*barra_size)


def ler():
    contatos = []
    try:
        with open('dados.json', 'r') as file:
            agenda_externa = json.load(file)
            for contato in agenda_externa:
                print(agenda_externa[contato])
                nome = agenda_externa[contato]['nome']
                telefone = agenda_externa[contato]['telefone']
                email = agenda_externa[contato]['email']
                twitter = agenda_externa[contato]['twitter']
                instagram = agenda_externa[contato]['instagram']
                contact = adicionar(nome, telefone, email, twitter, instagram)
                print(contact)
                contatos.append(contact)
            file.close()
            return contatos
    except FileNotFoundError:
        gravar({})
        return contatos


def gravar(listaDeContatos):
    agenda = {}
    contador = 0
    for contato in listaDeContatos:
        newContato = {}
        newContato['nome'] = contato.getNome()
        newContato['telefone'] = contato.getTelefone()
        newContato['email'] = contato.getEmail()
        newContato['twitter'] = contato.getTwitter()
        newContato['instagram'] = contato.getInstagram()
        agenda[contador] = newContato
        contador += 1
    with open('dados.json', 'w') as file:
        json.dump(agenda, file, indent=2)
        file.close()


def selecionaOpcao():
    print('Cadastrar contato -> 1')
    print('Buscar contato -> 2')
    print('Apagar contato -> 3')
    print('Atualizar contato -> 4')
    print('Listar todos os contatos -> 5')
    print('Sair -> 6\n')
    option = input('Selecione uma opção: ')
    return option


def adicionar(nome, telefone, email, twitter, instagram):
    novo_contato = Contato(nome, telefone, email, twitter, instagram)
    return novo_contato


def buscar(contatos, nome):
    if len(contatos) != 0:
        for contato in contatos:
            if contato.getNome() == nome:
                nome = contato.getNome()
                telefone = contato.getTelefone()
                email = contato.getEmail()
                twitter = contato.getTwitter()
                instagram = contato.getInstagram()
                print(f'{nome} - {telefone}')
                print(f'{email}')
                print(f'{twitter} | {instagram}')
                return
        print('Contato não encontrado!')
    else:
        print('Lista está vazia!')


def deletarContato(contatos, nome):
    if len(contatos) != 0:
        contador = 0
        for contato in contatos:
            if contato.getNome() == nome:
                contatos.pop(contador)
                print(f'Contato {nome} removido com sucesso!')
                return
            contador += 1
        print('Contato não encontrado!')
    else:
        print('Lista está vazia!')


def atualizar(contatos, nome):
    if len(contatos) != 0:
        for contato in contatos:
            if contato.getNome() == nome:
                print('Selecione um dado para ser atualizado:\n')
                print('Nome -> 1')
                print('Telefone -> 2')
                print('Email -> 3')
                print('Twitter -> 4')
                print('Instagram -> 5')
                while True:
                    dado = int(input())
                    if (dado == 1):
                        contato.setNome()
                        return
                    if (dado == 2):
                        contato.setTelefone()
                        return
                    if (dado == 3):
                        contato.setEmail()
                        return
                    if (dado == 4):
                        contato.setTwitter()
                        return
                    if (dado == 5):
                        contato.setInstagram()
                        return
                    print('Opção inválida!')
        print('Contato não encontrado!')
    else:
        print('Lista está vazia!')
