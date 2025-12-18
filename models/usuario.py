class Usuario:
    def __init__(self, nome: str, email: str, senha: str, perfil, id: int = None):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__perfil = perfil

    # GETTERS
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

    def get_perfil(self):
        return self.__perfil

    # SETTERS
    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_senha(self, senha):
        self.__senha = senha

    def set_perfil(self, perfil):
        self.__perfil = perfil

    def validarDados(self):
        if not self.__nome or not self.__email or not self.__senha:
            raise ValueError("Nome, email e senha são obrigatórios")

        if "@" not in self.__email:
            raise ValueError("Email inválido")
