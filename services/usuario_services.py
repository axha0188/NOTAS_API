from models.usuario_model import usuario_model
from schemas.usuario_schema import UsuarioSchema
from db.conexion import conn
from helpers.error_db_decorador import error_transaccion,cerrar_sesion


class UsuarioServices:
    @cerrar_sesion
    def listar_todos(self):
        return conn.execute(usuario_model.select()).fetchall()   

    @error_transaccion
    def grabar_registro(self, registro: UsuarioSchema):
        datos = {
            "nombre_usuario": registro.nombre_usuario,
            "nombre": registro.nombre,
            "apellido": registro.apellido,
            "correo": registro.correo,
            "clave": registro.clave,
            "estado": registro.estado,
            "creado": registro.creado,
        }
        conn.execute(usuario_model.insert().values(datos))

    @cerrar_sesion
    def obtener_registro(self, id: int):
        registro = conn.execute(usuario_model.select().where(
            usuario_model.c.id == id
        )).fetchall()
        if len(registro) == 0:
            return {}
        return registro

    @error_transaccion
    def actualizar_registro(self, registro: UsuarioSchema):
        conn.execute(
            usuario_model.update().values(
                nombre_usuario=registro.nombre_usuario,
                nombre=registro.nombre,
                apellido=registro.apellido,
                correo=registro.correo,
                clave=registro.clave,
                estado=registro.estado,
            )
            .where(usuario_model.c.id == registro.id)
        )

    @error_transaccion
    def eliminar_registro(self, id: int):
        conn.execute(usuario_model.delete().where(usuario_model.c.id == id))
        
