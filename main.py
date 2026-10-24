"""Orquestrador: pesquisador -> resumidor -> revisor -> redator.

Uso:
    python main.py "tema da pesquisa"
"""

import sys
from datetime import date

import config  # carrega o .env e valida a chave antes de tudo
from agents import pesquisar, redigir, resumir, revisar
from tools.arquivos import gerar_prefixo, salvar_saida


def main():
    if len(sys.argv) < 2:
        sys.exit('Uso: python main.py "tema da pesquisa"')
    tema = " ".join(sys.argv[1:])
    prefixo = gerar_prefixo(tema)
    print(f"Modelo: {config.MODELO}")

    print("1/4 Pesquisando...")
    material = pesquisar(tema)

    print("2/4 Resumindo...")
    resumo = resumir(tema, material)

    print("3/4 Revisando o resumo...")
    resumo_revisado, alteracoes = revisar(tema, material, resumo)
    caminho_revisao = salvar_saida(
        prefixo,
        "revisao",
        f"# Revisão do resumo: {tema}\n\n"
        f"Data: {date.today():%d/%m/%Y}\n\n"
        f"## O que o revisor alterou\n\n{alteracoes}\n",
    )

    print("4/4 Escrevendo o relatório...")
    relatorio = redigir(tema, resumo_revisado)
    caminho_relatorio = salvar_saida(prefixo, "relatorio", relatorio)

    print("Pronto!")
    print(f"  Relatório: {caminho_relatorio}")
    print(f"  Revisão:   {caminho_revisao}")


if __name__ == "__main__":
    main()
