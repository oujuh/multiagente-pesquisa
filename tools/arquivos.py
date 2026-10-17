"""Ferramenta para salvar os relatórios na pasta outputs/."""

import re
import unicodedata
from datetime import datetime

import config


def salvar_relatorio(tema, conteudo):
    """Salva o relatório em outputs/ e devolve o caminho do arquivo."""
    texto = unicodedata.normalize("NFKD", tema).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "_", texto.lower()).strip("_")[:50] or "relatorio"
    nome = f"{datetime.now():%Y%m%d_%H%M}_{slug}.md"
    caminho = config.PASTA_OUTPUTS / nome
    caminho.write_text(conteudo, encoding="utf-8")
    return caminho
