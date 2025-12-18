class usuario:
    def __init__(self, id, nome, email, senha, perfil):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__perfil = perfil

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha
    def get_perfil(self): return self.__perfil
