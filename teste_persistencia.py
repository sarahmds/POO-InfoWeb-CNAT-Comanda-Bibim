from database import Database
from models.prato import Prato
from dao.prato_dao import PratoDAO


print("=== TESTE DE PERSISTÊNCIA ===")

Database.criar_tabelas()

prato = Prato("Kimchi", "conserva coreana tradicional de vegetais fermentados", 35.0)
PratoDAO.inserir(prato)

prato = Prato("Tteokbokki", "Bolinhos de arroz cilíndricos e macios cozidos em um molho espesso, picante e levemente adocicado de gochujang.", 35.0)
PratoDAO.inserir(prato)

print("Pratos no banco:")
for p in PratoDAO.listar():
    print(p)
