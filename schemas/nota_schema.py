from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class NotaSchema(BaseModel):
    id: Optional[int]
    tipo: int
    titulo: str
    descripcion: str
    estado: bool
    creado: datetime
    usuario: int
