"""Agente pesquisador: busca na web e devolve material bruto com fontes."""

from agents.base import Agente
from tools.busca_web import FERRAMENTA_BUSCA

_agente = Agente(
    nome="Pesquisador",
    system=(
        "Você é um agente pesquisador. Pesquise o tema na web, cruzando mais de uma "
        "fonte. Devolva um material bruto organizado: fatos, dados e números "
        "relevantes, cada um com a URL da fonte. Não invente nada; se algo não for "
        "confirmado, diga isso."
    ),
    tools=FERRAMENTA_BUSCA,
)


def pesquisar(tema):
    return _agente.rodar(f"Tema da pesquisa: {tema}")
