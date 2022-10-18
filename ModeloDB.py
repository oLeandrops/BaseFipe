from lib2to3.pytree import convert
from sqlalchemy import create_engine,Column,Integer,String,select
from sqlalchemy.orm import sessionmaker, scoped_session
from  sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///tabelaFipe.db', echo=True, convert_unicode=True)

Base = declarative_base()

sessao = scoped_session(
    sessionmaker(
        autocommit=False,
        bind=engine
    )
)
Base.query = sessao.query_property()

class Carros(Base):
    __tablename__ = 'carros'
    id = Column(Integer,primary_key=True)
    fabricante = Column(String(100)) 
    modelo = Column(String(100))
    anoModelo = Column(String(100))
    versao = Column(String(100))
    codigoFipe = Column(String(100))
    precoMedio = Column(String(100))
    ultimaVariacao = Column(String(100))
    mesReferencia = Column(String(100))
    categoria = Column(String(100))

    def __repr__(self):
        return f'{self.id},{self.fabricante},{self.modelo},{self.anoModelo},{self.versao},{self.codigoFipe},{self.precoMedio},{self.ultimaVariacao}'

    

    def save(self):
        sessao.add(self)
        sessao.commit()


class Links(Base):
    __tablename__ = 'links'
    id = Column(Integer,primary_key=True)
    marca = Column(String(100)) 
    linkMarca = Column(String(100))
    modelo = Column(String(100)) 
    linkmodelo= Column(String(100))


    def __repr__(self):
        return f'{self.marca},{self.modelo}'

    def save(self):
        sessao.add(self)
        sessao.commit()

    






class Categoria(Base):
    __tablename__ = 'categoria'
    id = Column(Integer,primary_key=True)
    marca = Column(String(100))
    carro = Column(String(100))
    modelo = Column(String(100))
    status = Column(Integer)

    def __repr__(self):
        return f'{self.marca},{self.carro},{self.modelo}'

    def save(self):
        sessao.add(self)
        sessao.commit()


    



def create_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_database()






    


    


