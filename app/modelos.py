from typing import Optional

from pydantic import BaseModel

from .data import OpcoesDeStatus


class ModeloDoItem(BaseModel):
    # id: int
    titulo: str
    descrição: str
    status: Optional[OpcoesDeStatus]


class ModeloDoItemResposta(ModeloDoItem):
    id: int
