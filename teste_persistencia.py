from database import Database
from models.prato import Prato
from dao.prato_dao import PratoDAO
from models.mesa import Mesa
from dao.mesa_dao import MesaDAO


print("=== TESTE DE prato ===")

Database.criar_tabelas()

prato = Prato("Kimchi", "conserva coreana tradicional de vegetais fermentados", 35.0)
PratoDAO.inserir(prato)

prato = Prato("Tteokbokki", "Bolinhos de arroz cilíndricos e macios cozidos em um molho espesso, picante e levemente adocicado de gochujang.", 35.0)
PratoDAO.inserir(prato)

print("Pratos no banco:")
for p in PratoDAO.listar():
    print(p)



print("=== TESTE DE MESA ===")

Database.criar_tabelas()

mesa1 = Mesa(1)  
MesaDAO.inserir(mesa1)

mesa2 = Mesa(2, "OCUPADA")
MesaDAO.inserir(mesa2)

print("Mesas no banco:")
for m in MesaDAO.listar():
    print(m)

