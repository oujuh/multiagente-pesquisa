"""Ferramenta de busca na web, executada pelo servidor da API.

A busca precisa estar habilitada no Console da sua organização.
"""

import config

FERRAMENTA_BUSCA = [
    {"type": "web_search_20250305", "name": "web_search", "max_uses": config.MAX_BUSCAS}
]
