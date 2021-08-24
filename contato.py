class Contato():
    def __init__(self, nome, telefone, email, twitter, instagram):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__twitter = twitter
        self.__instagram = instagram

    def setNome(self):
        self.__nome = input('\nDigite o novo nome: ')

    def getNome(self):
        return self.__nome

    def setTelefone(self):
        self.__telefone = int(input('\nDigite o novo numero de telefone: '))

    def getTelefone(self):
        return self.__telefone

    def setEmail(self):
        self.__email = input('\nDigite o novo email: ')

    def getEmail(self):
        return self.__email

    def setTwitter(self):
        self.__twitter = input('\nDigite o novo twitter: ')

    def getTwitter(self):
        return self.__twitter

    def setInstagram(self):
        self.getInstagram = input('\nDigite o novo Instagram: ')

    def getInstagram(self):
        return self.__instagram
