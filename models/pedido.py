from datetime import datetime

class Pedido:
    def __init__(self, id=None, mesa=None, garcom=None, status="ABERTO", dataHora=None, total=0.0, dia_id=None):
        self.id = id
        self.mesa = mesa            # id da mesa
        self.garcom = garcom        # id do garçom
        self.status = status
        self.dataHora = dataHora if dataHora else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.total = total
        self.dia_id = dia_id        # id do dia em que o pedido foi feito

    # ===== GETTERS =====
    def get_id(self):
        return self.id

    def get_mesa(self):
        return self.mesa

    def get_garcom(self):
        return self.garcom

    def get_status(self):
        return self.status

    def get_dataHora(self):
        return self.dataHora

    def get_total(self):
        return self.total

    def get_dia_id(self):
        return self.dia_id

    # ===== SETTERS / ATUALIZAÇÕES =====
    def atualizarStatus(self, status):
        self.status = status

    def atualizarTotal(self, total):
        self.total = total

    def atualizarDia(self, dia_id):
        self.dia_id = dia_id

    # ===== CÁLCULO DE TOTAL (somando itens) =====
    def calcularTotal(self, itens=[]):
        """
        Calcula o total do pedido com base nos itens.
        Cada item deve ter:
        - get_quantidade()
        - get_prato() -> get_preco()
        """
        total = 0.0
        for item in itens:
            total += item.get_quantidade() * item.get_prato().get_preco()
        self.total = total
        return total

    # ===== REPRESENTAÇÃO LEGÍVEL =====
    def __str__(self):
        return f"Pedido {self.id} - Mesa: {self.mesa}, Garçom: {self.garcom}, Status: {self.status}, Total: R$ {self.total:.2f}, Dia ID: {self.dia_id}"
