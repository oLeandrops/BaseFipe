from re import L
from ModeloDB import sessao, Carros, Categoria, Links


def cadastrarCarro(fabricante,modelo,anoModelo,versao,codigofipe,preco,ultimaVariacao,mesReferencia,categoria):
    carros = Carros(
        fabricante=fabricante,modelo=modelo,anoModelo=anoModelo,versao=versao,codigoFipe=codigofipe,precoMedio=preco,
        ultimaVariacao=ultimaVariacao,mesReferencia=mesReferencia,categoria=categoria
        )
    carros.save()
    print('Carro cadastrado Com sucesso')



def cadastrarlink(marca,linkmarca,modelo,linkmodelo):
    link = Links(
        marca=marca,
        linkMarca=linkmarca,
        modelo=modelo,
        linkmodelo=linkmodelo
        )
    link.save()
    print('link cadastrado Com sucesso')


def consultalink():
    links = Links.query.filter(Links.linkMarca==None).first()
    url = links.linkmodelo
    id = links.id
    return url, id


def atualizarlink(id):
    links = Links.query.filter(Links.id==id).first()
    links.linkMarca = 'OK'
    links.save()


def consulta(carro):
    categoria = Categoria.query.filter(Categoria.carro==carro).first()
    marca = categoria.marca
    nomeCarro = categoria.carro
    nomeModelo = categoria.modelo
    print(f'{marca},{nomeCarro},{nomeModelo}')


def select_all():
    categoria = Categoria.query.all()
    for p in categoria:
        print(p.marca, p.carro, p.modelo)

def teste():
    print('teste')

if __name__ == '__main__':
    #inserircarro('fiat','palio','2022')
    #consulta('palio')
    #select_all()
    consultalink()