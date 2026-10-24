# Multiagente de pesquisa

Pipeline com quatro agentes: **pesquisador → resumidor → revisor → redator**.

O revisor confere o resumo contra o material bruto da pesquisa, corrige o que
for necessário e registra cada alteração em um arquivo separado.

## Estrutura

```
multiagente_pesquisa/
├── main.py            # orquestrador (ponto de entrada)
├── config.py          # configurações e leitura do .env
├── .env               # sua chave da API (não compartilhe!)
├── requirements.txt
├── agents/            # um arquivo por agente (pesquisador, resumidor, revisor, redator)
├── tools/             # busca na web e salvamento de arquivos
└── outputs/           # arquivos gerados
```

## Como usar

1. Cole sua chave no arquivo `.env`.
2. Instale as dependências: `python -m pip install -r requirements.txt`
3. Rode: `python main.py "tema da pesquisa"`

## Saídas (pasta outputs/)

Cada execução gera dois arquivos com o mesmo prefixo (data, hora e tema):

- `..._relatorio.md`: o relatório final.
- `..._revisao.md`: a lista do que o revisor alterou no resumo, e por quê.

O modelo padrão é o mais barato (Haiku); para trocar, descomente a linha
`MODELO=` no `.env`.
