from services.usuario_services import UsuarioServices
from schemas.usuario_schema import UsuarioSchema


class UsuarioControllers:
    def __init__(self) -> None:
        self.__controller = UsuarioServices()

    def listar_todos_async(self):
        return self.__controller.listar_todos()

    def grabar_registro_async(self, registro: UsuarioSchema):
        self.__controller.grabar_registro(registro)

    def obtener_registro_async(self, id: int):
        return self.__controller.obtener_registro(id)

    def actualizar_registro_async(self, registro: UsuarioSchema):
        self.__controller.actualizar_registro(registro)

    def eliminar_registro_async(self, id: int):
        self.__controller.eliminar_registro(id)
