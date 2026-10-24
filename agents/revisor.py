"""Agente revisor: confere o resumo contra o material bruto e corrige o necessário."""

from agents.base import Agente

MARCA_RESUMO = "===RESUMO REVISADO==="
MARCA_ALTERACOES = "===ALTERACOES==="

_agente = Agente(
    nome="Revisor",
    system=(
        "Você é um agente revisor. Receba o material bruto de uma pesquisa e o resumo "
        "produzido por outro agente. Compare o resumo com o material bruto e corrija: "
        "afirmações sem apoio no material, números ou datas divergentes, URLs que não "
        "constem no material, redundâncias, trechos ambíguos, omissões de pontos "
        "importantes e divergências entre fontes que não foram sinalizadas. "
        "Faça apenas as alterações necessárias, mantendo a estrutura e as URLs. "
        "Não acrescente nenhuma informação que não esteja no material bruto.\n\n"
        "Responda EXATAMENTE neste formato, sem texto fora dele:\n\n"
        f"{MARCA_RESUMO}\n"
        "(o resumo completo, já corrigido)\n"
        f"{MARCA_ALTERACOES}\n"
        "(lista numerada com cada alteração: o que mudou, onde e por quê. "
        "Se não houve mudanças, escreva: Nenhuma alteração necessária.)"
    ),
    max_tokens=6000,
)


def revisar(tema, material, resumo):
    """Devolve (resumo_revisado, alteracoes)."""
    resposta = _agente.rodar(
        f"Tema: {tema}\n\n"
        f"--- MATERIAL BRUTO ---\n{material}\n\n"
        f"--- RESUMO A REVISAR ---\n{resumo}"
    )

    if MARCA_RESUMO in resposta and MARCA_ALTERACOES in resposta:
        parte_resumo, parte_alteracoes = resposta.split(MARCA_ALTERACOES, 1)
        resumo_revisado = parte_resumo.split(MARCA_RESUMO, 1)[1].strip()
        alteracoes = parte_alteracoes.strip()
        if resumo_revisado:
            return resumo_revisado, alteracoes

    # Resposta fora do formato: mantém o resumo original e avisa no registro.
    aviso = (
        "Aviso: a resposta do revisor veio fora do formato esperado. "
        "O resumo original foi mantido sem alterações.\n\n"
        f"Resposta bruta do revisor:\n\n{resposta}"
    )
    return resumo, aviso
