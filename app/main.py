import streamlit as st
from dotenv import load_dotenv

from utils.leitor_pdf import carregar_pdf, separar_em_blocos
from utils.logica_ia import criar_banco_vetores, criar_chain_agente
from utils.chat import main_chat

load_dotenv()


if __name__ == "__main__":
        
    texto_pdf = carregar_pdf()

    lista_blocos = separar_em_blocos(texto_pdf)

    banco_vetores = criar_banco_vetores(lista_blocos)

    # carregar chain e vector store
    chain = criar_chain_agente(banco_vetores)

    main_chat(chain)

