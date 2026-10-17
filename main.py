"""Orquestrador: pesquisador -> resumidor -> redator.

Uso:
    python main.py "tema da pesquisa"
"""

import sys

import config  # carrega o .env e valida a chave antes de tudo
from agents import pesquisar, redigir, resumir
from tools.arquivos import salvar_relatorio


def main():
    if len(sys.argv) < 2:
        sys.exit('Uso: python main.py "tema da pesquisa"')
    tema = " ".join(sys.argv[1:])
    print(f"Modelo: {config.MODELO}")

    print("1/3 Pesquisando...")
    material = pesquisar(tema)

    print("2/3 Resumindo...")
    resumo = resumir(tema, material)

    print("3/3 Escrevendo o relatório...")
    relatorio = redigir(tema, resumo)

    caminho = salvar_relatorio(tema, relatorio)
    print(f"Pronto! Relatório salvo em {caminho}")


if __name__ == "__main__":
    main()
