"""Classe base: todo agente é um modelo + um papel (system prompt) + ferramentas."""

import anthropic

import config

client = anthropic.Anthropic(api_key=config.API_KEY)


class Agente:
    def __init__(self, nome, system, tools=None, max_tokens=4000):
        self.nome = nome
        self.system = system
        self.tools = tools
        self.max_tokens = max_tokens

    def rodar(self, pedido):
        """Executa o agente, tratando as pausas da busca na web."""
        mensagens = [{"role": "user", "content": pedido}]
        resp = None
        for _ in range(5):
            kwargs = dict(
                model=config.MODELO,
                max_tokens=self.max_tokens,
                system=self.system,
                messages=mensagens,
            )
            if self.tools:
                kwargs["tools"] = self.tools
            resp = client.messages.create(**kwargs)
            if resp.stop_reason != "pause_turn":
                break
            # A busca server-side pode pausar o turno; continua de onde parou.
            mensagens.append({"role": "assistant", "content": resp.content})
        return "".join(b.text for b in resp.content if b.type == "text")
