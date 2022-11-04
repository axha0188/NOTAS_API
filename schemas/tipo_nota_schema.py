from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TipoNotaSchema(BaseModel):
    id: Optional[int]
    titulo:str
    descripcion: str
    estado: bool
    creado: datetime
    usuario: int