"""
Ponto de entrada do Edu.

Ideia geral do fluxo:
1. Carregar o conteúdo de AGENT.md e knowledge.md (texto puro).
2. Carregar os dados de data/ que o Edu vai usar para responder.
3. Montar um system prompt juntando os dois.
4. Rodar uma interface (ex: Streamlit) que manda a pergunta do usuário +
   system prompt + dados para uma LLM, e mostra a resposta.

Cada função abaixo é uma decisão sua. Os TODOs são pontos de partida,
não a solução pronta.
"""


def carregar_agente() -> str:
    """Lê AGENT.md e knowledge.md e retorna o texto que vira o system prompt."""
    # TODO: abrir os dois arquivos e juntar o conteúdo em uma única string
    raise NotImplementedError


def carregar_dados():
    """Lê os arquivos de data/ que o Edu vai consultar."""
    # TODO: qual formato são os dados (CSV, JSON)? Qual biblioteca ajuda a ler isso?
    raise NotImplementedError


def perguntar_a_llm(pergunta: str, system_prompt: str, dados) -> str:
    """Envia a pergunta do cliente para a LLM, junto com o contexto do Edu."""
    # TODO: escolher o provedor da LLM (ex: Claude, OpenAI) e configurar o cliente
    raise NotImplementedError


def main():
    # TODO: montar a interface de chat (ex: Streamlit) que chama as funções acima
    pass


if __name__ == "__main__":
    main()
