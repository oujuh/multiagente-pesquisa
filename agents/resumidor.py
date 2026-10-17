"""Agente resumidor: condensa o material bruto mantendo as fontes."""

from agents.base import Agente

_agente = Agente(
    nome="Resumidor",
    system=(
        "Você é um agente resumidor. Receba material de pesquisa e produza um resumo "
        "estruturado: agrupe por subtemas, elimine redundâncias, destaque pontos de "
        "divergência entre fontes e mantenha a URL junto de cada afirmação."
    ),
)


def resumir(tema, material):
    return _agente.rodar(f"Tema: {tema}\n\nMaterial bruto:\n{material}")
