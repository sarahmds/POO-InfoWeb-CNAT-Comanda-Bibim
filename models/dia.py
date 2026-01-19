class Dia:
    def __init__(self, id=None, data=None, aberto=0):
        self.id = id
        self.data = data
        self.aberto = aberto

    def get_id(self):
        return self.id

    def get_data(self):
        return self.data

    def get_aberto(self):
        return self.aberto

    def abrir(self):
        self.aberto = 1

    def fechar(self):
        self.aberto = 0
