from database import Database
from models.prato import Prato
from dao.prato_dao import PratoDAO

print("=== TESTE DE PERSISTÊNCIA ===")

Database.criar_tabelas()

prato = Prato(0, "Pizza", "Italiana", 35.0)
PratoDAO.inserir(prato)
print("Prato salvo no banco.")

pratos = PratoDAO.listar()
print("Pratos recuperados do banco:")
for p in pratos:
    print(p)
