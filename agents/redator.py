"""Agente redator: transforma o resumo em um relatório em Markdown."""

from datetime import date

from agents.base import Agente

_agente = Agente(
    nome="Redator",
    system=(
        "Você é um agente redator. Escreva um relatório em português, em Markdown, "
        "com: título, resumo executivo, seções de desenvolvimento, conclusão e "
        "referências. Use apenas informações e URLs presentes no resumo recebido; "
        "não acrescente fontes."
    ),
    max_tokens=6000,
)


def redigir(tema, resumo):
    return _agente.rodar(
        f"Tema: {tema}\nData: {date.today():%d/%m/%Y}\n\nResumo:\n{resumo}"
    )
