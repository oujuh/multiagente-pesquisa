"""Configurações centrais do projeto."""

import os
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")

API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
if not API_KEY or API_KEY.startswith("cole-"):
    raise SystemExit(
        "Chave da API não encontrada. Abra o arquivo .env e cole sua chave "
        "em ANTHROPIC_API_KEY."
    )

# Modelo mais barato da família atual (Haiku). Pode ser trocado no .env.
MODELO = os.getenv("MODELO", "claude-haiku-5-5")

# Quantidade máxima de buscas na web por pesquisa.
MAX_BUSCAS = int(os.getenv("MAX_BUSCAS", "6"))

PASTA_OUTPUTS = RAIZ / "outputs"
PASTA_OUTPUTS.mkdir(exist_ok=True)
