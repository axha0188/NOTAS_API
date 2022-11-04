from fastapi import APIRouter
from typing import Union, List
from starlette.status import HTTP_200_OK
from schemas.usuario_schema import UsuarioSchema
from controllers.usuario_controllers import UsuarioControllers

usuario_route = APIRouter()


@usuario_route.get(
    "/api/usuario",
    tags=["Usuario"],
    response_model=List[UsuarioSchema],
    description="lista todos los usuarios",
)
def listar_todos():
    return UsuarioControllers().listar_todos_async()


@usuario_route.post(
    "/api/usuario",
    tags=["Usuario"],
    status_code=HTTP_200_OK,
    description="graba un usuario",
)
def grabar_registro(registro: UsuarioSchema):
    UsuarioControllers().grabar_registro_async(registro)
    return HTTP_200_OK


@usuario_route.get(
    "/api/usuario/{id}",
    tags=["Usuario"],
    response_model=Union[List[UsuarioSchema], dict],
    description="obtener un usuario por id",
)
def obtener_registro(id: int):
    return UsuarioControllers().obtener_registro_async(id)


@usuario_route.put(
    "/api/usuario",
    tags=["Usuario"],
    status_code=HTTP_200_OK,
    description="actualizar usuario por id",
)
def actualizar(registro: UsuarioSchema):
    UsuarioControllers().actualizar_registro_async(registro)
    return HTTP_200_OK


@usuario_route.delete(
    "/api/usuario/{id}",
    tags=["Usuario"],
    status_code=HTTP_200_OK,
    description="eliminar usuario por id"
)
def eliminar(id: int):
    UsuarioControllers().eliminar_registro_async(id)
    return HTTP_200_OK
