from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from database import engine

Base = declarative_base()

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    autor = Column(String(255), nullable=False)
    genero = Column(String(100), nullable=False)
    leido = Column(String(10), nullable=False)

    def __repr__(self):
        return f"<Libro(id={self.id}, titulo={self.titulo})>"

Base.metadata.create_all(engine)
