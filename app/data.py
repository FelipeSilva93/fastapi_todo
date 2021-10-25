from enum import Enum
from typing import Any, Dict, List, Optional, Union


class OpcoesDeStatus(str, Enum):
    a_fazer = "a fazer"
    fazendo = "fazendo"
    feito = "feito"


Item = Dict[str, Union[int, str, OpcoesDeStatus]]


class AFazer:
    todo: List[Item] = [
        {
            "id": 1,
            "titulo": "fazer live",
            "descrição": "Fazer live na twitch",
            "status": OpcoesDeStatus.a_fazer,
        },
        {
            "id": 2,
            "titulo": "escovar os dentes",
            "descrição": "escovar os dentes pela manhã",
            "status": OpcoesDeStatus.fazendo,
        },
        {
            "id": 3,
            "titulo": "dormir",
            "descrição": "dormir a tarde",
            "status": OpcoesDeStatus.feito,
        },
    ]

    id_atual = 3

    def listar(self):
        return self.todo

    def inserir(self, item: Item) -> Item:
        self.id_atual += 1
        item["id"] = self.id_atual
        self.todo.append(item)
        return item

    def pegar(self, id_item: int) -> Item:
        item = filter(lambda x: x["id"] == id_item, self.todo)
        return list(item)[0]

    def filtrar(self, status: OpcoesDeStatus) -> List[Item]:
        return list(filter(lambda x: x["status"] == status, self.todo))
