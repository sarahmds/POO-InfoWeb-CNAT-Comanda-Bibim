from database import Database
from models.prato import Prato
from models.mesa import Mesa
from models.usuario import Usuario
from models.pedido import Pedido
from models.item_pedido import ItemPedido
from dao.prato_dao import PratoDAO
from dao.mesa_dao import MesaDAO
from dao.usuario_dao import UsuarioDAO
from dao.pedido_dao import PedidoDAO
from dao.itempedido_dao import ItemPedidoDAO


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


print("=== TESTE DE USUÁRIO ===")

Database.criar_tabelas()

u1 = Usuario("João Silva", "joao@example.com", "1234", "GARCOM")
UsuarioDAO.inserir(u1)

u2 = Usuario("Maria Souza", "maria@example.com", "abcd", "GERENTE")
UsuarioDAO.inserir(u2)

u3 = Usuario("Cristina morais", "Cristina@example.com", "abcd", "CHEFE")
UsuarioDAO.inserir(u3)

print("Usuários no banco:")
for u in UsuarioDAO.listar():
    print(u)



print("=== TESTE DE PEDIDO E ITEM_PEDIDO ===")

Database.criar_tabelas()

prato1 = Prato("Kimchi", "Conserva coreana", 35.0)
prato2 = Prato("Tteokbokki", "Bolinhos de arroz", 40.0)
PratoDAO.inserir(prato1)
PratoDAO.inserir(prato2)

pratos = PratoDAO.listar()
p1, p2 = pratos[0], pratos[1]

pedido = Pedido(mesa=1, garcom=1, status="ABERTO")
pedido.adicionarItem(p1.get_id(), 2, p1.get_preco())  
pedido.adicionarItem(p2.get_id(), 1, p2.get_preco())  
PedidoDAO.inserir(pedido)

pedido_real = PedidoDAO.listar()[0]
pedido._Pedido__id = pedido_real.get_id() 

item1 = ItemPedido(prato=p1, quantidade=2, pedido=pedido)
item2 = ItemPedido(prato=p2, quantidade=1, pedido=pedido)
ItemPedidoDAO.inserir(item1)
ItemPedidoDAO.inserir(item2)

print("Pedidos no banco:")
for ped in PedidoDAO.listar():
    print(f"Pedido {ped.get_id()} - Mesa {ped.get_mesa()} - Garçom {ped.get_garcom()} - Status {ped.get_status()} - Total R$ {ped.calcularTotal():.2f}")

print("Itens de pedido no banco:")
for item in ItemPedidoDAO.listar():
    print(item)
