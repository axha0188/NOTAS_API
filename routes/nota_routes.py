from fastapi import APIRouter
from typing import Union, List
from starlette.status import HTTP_200_OK
from schemas.nota_schema import NotaSchema
from controllers.nota_controllers import NotaControllers

nota_route = APIRouter()


@nota_route.get(
    "/api/nota",
    tags=["Nota"],
    response_model=List[NotaSchema],
    description="lista todos los notas",
)
def listar_todos():
    return NotaControllers().listar_todos_async()


@nota_route.post(
    "/api/nota",
    tags=["Nota"],
    status_code=HTTP_200_OK,
    description="graba un nota",
)
def grabar_registro(registro: NotaSchema):
    NotaControllers().grabar_registro_async(registro)
    return HTTP_200_OK


@nota_route.get(
    "/api/nota/{id}",
    tags=["Nota"],
    response_model=Union[List[NotaSchema], dict],
    description="obtener una nota por id",
)
def obtener_registro(id: int):
    return NotaControllers().obtener_registro_async(id)


@nota_route.put(
    "/api/nota",
    tags=["Nota"],
    status_code=HTTP_200_OK,
    description="actualizar nota por id",
)
def actualizar(registro: NotaSchema):
    NotaControllers().actualizar_registro_async(registro)
    return HTTP_200_OK


@nota_route.delete(
    "/api/nota/{id}",
    tags=["Nota"],
    status_code=HTTP_200_OK,
    description="eliminar nota por id"
)
def eliminar(id: int):
    NotaControllers().eliminar_registro_async(id)
    return HTTP_200_OK
