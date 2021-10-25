from typing import Any, Dict, List, Optional

from fastapi.routing import APIRouter

from .data import AFazer, OpcoesDeStatus
from .modelos import ModeloDoItem, ModeloDoItemResposta

router = APIRouter()
todo = AFazer()


@router.get("/", response_model=List[ModeloDoItemResposta])
def listar_a_fazer(status: Optional[OpcoesDeStatus] = None):
    """
    View que retorna a lista de itens a Fazer
    """
    if status is not None:
        return todo.filtrar(status=status)
    else:
        return todo.listar()


@router.post("/", response_model=ModeloDoItemResposta, status_code=201)
def inserir_a_fazer(item_a_inserir: ModeloDoItem):
    """
    View que insere item na lista de itens a fazer
    """
    return todo.inserir(item_a_inserir.dict())


@router.get("/{id_do_item}", response_model=ModeloDoItemResposta)
def pegar_item_a_fazer(id_do_item: int):
    """
    View que mostra um item a partir do id dele
    """
    return todo.pegar(id_do_item)
