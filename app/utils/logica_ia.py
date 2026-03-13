from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


def criar_banco_vetores(lista_blocos):
    ferramenta_embedding = OpenAIEmbeddings(model="text-embedding-3-small")
    banco_vetores = FAISS.from_documents(lista_blocos, ferramenta_embedding)
    return banco_vetores

# logica do agente de IA
def criar_chain_agente(banco_vetores):

    prompt_template = ChatPromptTemplate.from_template(
        """Você é um assistente que responde perguntas sobre código de ética do banco Horizonte.
    Use APENAS as informações do contexto abaixo para responder.
    Se não encontrar a resposta, diga claramente que não sabe responder.
    Responda em português do Brasil, de forma clara e objetiva.

    Contexto: {context}

    A pergunta: {question}

    Resposta:"""
    )

    buscador_contexto = banco_vetores.as_retriever()

    llm = ChatOpenAI(model="gpt-4o-mini")

    chain = (
        {"context": buscador_contexto, "question": RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
    )

    return chain
