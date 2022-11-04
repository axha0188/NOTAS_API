from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Boolean,DATETIME
from db.conexion import meta, engine

tipo_nota_model = Table(
    "tbl_tipo_nota",
    meta,
    Column("id", Integer, primary_key=True),
    Column("titulo", String(20)),
    Column("descripcion", String(300)),
    Column("estado", Boolean),
    Column("creado", DATETIME),
    Column("usuario", Integer),
)

meta.create_all(engine)