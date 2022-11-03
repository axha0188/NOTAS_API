from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# VARIABLES .ENV
# EJEMPLO = "mysql+pymysql://root:@localhost:3306/FAST_API_CLOUD"
SERVIDOR = 'localhost'
PUERTO = '3306'
USUARIO = 'root'
CLAVE = ''
BASE_DE_DATOS = 'FAST_API_CLOUD'
CONEXION = f"mysql+pymysql://{USUARIO}:{CLAVE}@{SERVIDOR}:{PUERTO}/{BASE_DE_DATOS}"
engine = create_engine(CONEXION)
meta = MetaData()
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
