from typing import Optional
from pydantic import BaseModel, EmailStr


class UsuarioSchema(BaseModel):
    id: Optional[int]
    nombre_usuario: str
    nombre: str
    apellido: str
    correo: EmailStr
    clave: str
    estado: bool
    creado: str
    