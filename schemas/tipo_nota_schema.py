from typing import Optional
from pydantic import BaseModel


class TipoNotaSchema(BaseModel):
    id: Optional[int]
    titulo:str
    descripcion: str
    estado: bool
    creado: str
    usuario: int