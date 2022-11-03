from models.nota_model import nota_model
from schemas.nota_schema import NotaSchema
from db.conexion import conn
from helpers.error_db_decorador import error_transaccion,cerrar_sesion


class NotaServices:
    @cerrar_sesion
    def listar_todos(self):
        try:
            return conn.execute(nota_model.select()).fetchall()
        except Exception as error:
            return error

    @error_transaccion
    def grabar_registro(self, registro: NotaSchema):
        datos = {
            "tipo": registro.tipo,
            "titulo": registro.titulo,
            "descripcion": registro.descripcion,
            "estado": registro.estado,
            "creado": registro.creado,
            "usuario": registro.usuario
        }
        conn.execute(nota_model.insert().values(datos))

    @cerrar_sesion
    def obtener_registro(self, id: int):
        registro = conn.execute(nota_model.select().where(
            nota_model.c.id == id
        )).fetchall()
        if len(registro) == 0:
            return {}
        return registro

    @error_transaccion
    def actualizar_registro(self, registro: NotaSchema):
        conn.execute(
            nota_model.update().values(
                tipo=registro.tipo,
                titulo=registro.titulo,
                descripcion=registro.descripcion,
                estado=registro.estado,
            )
            .where(nota_model.c.id == registro.id)
        )

    @error_transaccion
    def eliminar_registro(self, id: int):
        try:
            conn.execute(nota_model.delete().where(nota_model.c.id == id))
        except:
            pass
