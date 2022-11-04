from models.tipo_nota_model import tipo_nota_model
from schemas.tipo_nota_schema import TipoNotaSchema
from db.conexion import conn
from helpers.error_db_decorador import error_transaccion, cerrar_sesion


class TipoNotaServices:
    @cerrar_sesion
    def listar_todos(self):
        return conn.execute(tipo_nota_model.select()).fetchall()

    @error_transaccion
    def grabar_registro(self, registro: TipoNotaSchema):
        datos = {
            "titulo": registro.titulo,
            "descripcion": registro.descripcion,
            "estado": registro.estado,
            "creado": registro.creado,
            "usuario": registro.usuario
        }
        conn.execute(tipo_nota_model.insert().values(datos))

    @cerrar_sesion
    def obtener_registro(self, id: int):
        registro = conn.execute(tipo_nota_model.select().where(
            tipo_nota_model.c.id == id
        )).fetchall()
        if len(registro) == 0:
            return {}
        return registro

    @error_transaccion
    def actualizar_registro(self, registro: TipoNotaSchema):
        conn.execute(
            tipo_nota_model.update().values(
                titulo=registro.titulo,
                descripcion=registro.descripcion,
                estado=registro.estado,
            )
            .where(tipo_nota_model.c.id == registro.id)
        )

    @error_transaccion
    def eliminar_registro(self, id: int):
        conn.execute(tipo_nota_model.delete().where(tipo_nota_model.c.id == id))
