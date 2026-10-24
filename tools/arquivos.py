"""Ferramentas para salvar os arquivos de saída na pasta outputs/."""

import re
import unicodedata
from datetime import datetime

import config


def gerar_prefixo(tema):
    """Cria o prefixo comum dos arquivos de uma execução (data, hora e tema)."""
    texto = unicodedata.normalize("NFKD", tema).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "_", texto.lower()).strip("_")[:50] or "pesquisa"
    return f"{datetime.now():%Y%m%d_%H%M}_{slug}"


def salvar_saida(prefixo, sufixo, conteudo):
    """Salva outputs/<prefixo>_<sufixo>.md e devolve o caminho do arquivo."""
    caminho = config.PASTA_OUTPUTS / f"{prefixo}_{sufixo}.md"
    caminho.write_text(conteudo, encoding="utf-8")
    return caminho
