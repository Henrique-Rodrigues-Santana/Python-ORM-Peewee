from database import db,Usuario,Anuncios


db.connect()

db.create_tables([Usuario,Anuncios])



#try:
#    Usuario.create(nome="henrique rodrigues",email="henrique@gmail.com",senha="123456")
#    Usuario.create(nome="marco",email="marco@gmail.com",senha="125556")
#    Usuario.create(nome="felipe",email="felipe@gmail.com",senha="78956")
#    Usuario.create(nome="manuela",email="manuela@gmail.com",senha="123456")
#    Usuario.create(nome="beta",email="beta@gmail.com",senha="123456")
#except:
#    print('Clientes já cadastrados.')


#lista_usuarios = Usuario.select()
#print("Listas de Usuarios:")

#for i in lista_usuarios:
#    print(i.id, i.nome, i.email)

#usuario1 = Usuario.get(Usuario.id == 1)
#print("Usuario 1: {}, id = {} ".format(usuario1.nome,usuario1.id))


#marco = Usuario.get(Usuario.email == "marco@gmail.com")
#marco.nome = " Maria Python lá ele"
#marco.save()

#print("O Usuario de id: {}, foi alterado o nome para {}".format(marco.id,marco.nome))

#usuario_deletado = Usuario.get(Usuario.email == "marco@gmail.com")
#usuario_deletado.delete_instance()

### testando se dado realmente foi deletado.

#try:
#    Usuario.get(Usuario.email == "marco@gmail.com")
#except:
#    print("Deu certo, o usuário foi deletado")


#felipe = Usuario.get(Usuario.email == "felipe@gmail.com")

#anuncio = Anuncios.create(
#    usuario = felipe,
#    titulo = "Anuncio 1",
#    descricao = "Descrição do anuncio 1",
#    valor = 100
#)

#print(anuncio.titulo)



#Anuncios.create(
#    usuario = felipe,
#    titulo = "Anuncio 2",
#    descricao = "Descrição do anuncio 1",
#    valor = 100
#)
#Anuncios.create(
#    usuario = felipe,
#   titulo = "Anuncio 3",
#    descricao = "Descrição do anuncio 1",
#    valor = 100
#)
#Anuncios.create(
#    usuario = felipe,
#   titulo = "Anuncio 4",
#    descricao = "Descrição do anuncio 1",
#    valor = 100
#)


#print("Anuncios de Maria: ")
#busque na tabela 'Anuncio', incluindo 'Usuario' onde o email 'Usuario.email' é igual a 'maria@gmail.com'
#anuncios_felipe = Anuncios.select().join(Usuario).where(Usuario.email == "felipe@gmail.com")

#for i in anuncios_felipe:
#    print('-  {}, {}, {}.'.format(i.id,i.titulo,i.valor) )

Anuncios.delete().execute()

print("Total de anuncios do usuario maria:{}".format(Anuncios.select().count()))