from fastapi import APIRouter
from typing import Union, List
from starlette.status import HTTP_200_OK
from schemas.tipo_nota_schema import TipoNotaSchema
from controllers.tipo_nota_controllers import TipoNotaControllers

tipo_nota_route = APIRouter()


@tipo_nota_route.get(
    "/api/tiponota",
    tags=["Tipo Nota"],
    response_model=List[TipoNotaSchema],
    description="lista todos los tipo notas",
)
def listar_todos():
    return TipoNotaControllers().listar_todos_async()


@tipo_nota_route.post(
    "/api/tiponota",
    tags=["Tipo Nota"],
    status_code=HTTP_200_OK,
    description="graba un tipo nota",
)
def grabar_registro(registro: TipoNotaSchema):
    TipoNotaControllers().grabar_registro_async(registro)
    return HTTP_200_OK


@tipo_nota_route.get(
    "/api/tiponota/{id}",
    tags=["Tipo Nota"],
    response_model=Union[List[TipoNotaSchema], dict],
    description="obtener un tipo nota por id",
)
def obtener_registro(id: int):
    return TipoNotaControllers().obtener_registro_async(id)


@tipo_nota_route.put(
    "/api/tiponota",
    tags=["Tipo Nota"],
    status_code=HTTP_200_OK,
    description="actualizar tipo nota por id",
)
def actualizar(registro: TipoNotaSchema):
    TipoNotaControllers().actualizar_registro_async(registro)
    return HTTP_200_OK


@tipo_nota_route.delete(
    "/api/tiponota/{id}",
    tags=["Tipo Nota"],
    status_code=HTTP_200_OK,
    description="eliminar tipo nota por id"
)
def eliminar(id: int):
    TipoNotaControllers().eliminar_registro_async(id)
    return HTTP_200_OK
