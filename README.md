# Multiagente de pesquisa

Pipeline com três agentes: **pesquisador → resumidor → redator**.

## Estrutura

```
multiagente_pesquisa/
├── main.py            # orquestrador (ponto de entrada)
├── config.py          # configurações e leitura do .env
├── .env               # sua chave da API (não compartilhe!)
├── requirements.txt
├── agents/            # um arquivo por agente
├── tools/             # busca na web e salvamento de arquivos
└── outputs/           # relatórios gerados (.md)
```

## Como usar

1. Cole sua chave no arquivo `.env`.
2. Instale as dependências: `python -m pip install -r requirements.txt`
3. Rode: `python main.py "tema da pesquisa"`

O relatório é salvo em `outputs/`. O modelo padrão é o mais barato (Haiku);
para trocar, descomente a linha `MODELO=` no `.env`.
