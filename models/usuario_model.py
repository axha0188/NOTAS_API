from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Boolean,DATETIME
from db.conexion import meta, engine

usuario_model = Table(
    "tbl_usuario",
    meta,
    Column("id", Integer, primary_key=True),
    Column("nombre_usuario", String(10), unique=True),
    Column("nombre", String(100)),
    Column("apellido", String(100)),
    Column("correo", String(100)),
    Column("clave", String(100)),
    Column("estado", Boolean),
    Column("creado", DATETIME),
    Column("usuario", Integer),
)

meta.create_all(engine)