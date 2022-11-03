from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Boolean,DATETIME
from db.conexion import meta, engine

nota_model = Table(
    "tbl_nota",
    meta,
    Column("id", Integer, primary_key=True),
    Column("tipo", Integer),
    Column("titulo", String(100)),
    Column("descripcion", String(500)),
    Column("estado", Boolean),
    Column("creado", DATETIME),
    Column("usuario", Integer),
)

meta.create_all(engine)
