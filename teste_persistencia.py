from database import Database
from models.prato import Prato
from dao.prato_dao import PratoDAO

print("=== TESTE DE PERSISTÊNCIA ===")

Database.criar_tabelas()

prato = Prato(None, "Kimchi", "Coreano", 35.0)
PratoDAO.inserir(prato)

print("Pratos no banco:")
for p in PratoDAO.listar():
    print(p)
