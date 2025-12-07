from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


USER = "root"
PASSWORD = "tu_password"
HOST = "localhost"
DB_NAME = "biblioteca"

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"

try:
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    print("✔ Conexión establecida con MariaDB")
except SQLAlchemyError as e:
    print(" Error de conexión con MariaDB:", e)
