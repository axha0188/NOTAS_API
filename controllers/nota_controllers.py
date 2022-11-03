from services.nota_services import NotaServices
from schemas.nota_schema import NotaSchema


class NotaControllers:
    def __init__(self) -> None:
        self.__controller = NotaServices()

    def listar_todos_async(self):
        return self.__controller.listar_todos()

    def grabar_registro_async(self, registro: NotaSchema):
        self.__controller.grabar_registro(registro)

    def obtener_registro_async(self, id: int):
        return self.__controller.obtener_registro(id)

    def actualizar_registro_async(self, registro: NotaSchema):
        self.__controller.actualizar_registro(registro)

    def eliminar_registro_async(self, id: int):
        self.__controller.eliminar_registro(id)
