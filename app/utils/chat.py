import streamlit as st


def main_chat(chain):
    
    st.set_page_config(layout="wide")

    st.set_page_config(
        page_title="Etica - Banco Horizonte",
        page_icon="🏦"
    )

    st.title(
        "Assistente RAG — Código de Ética 🏦", width="stretch", text_alignment="center"
    )
    
    # inicia a lista de mensagens
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # exibe as mensagens na tela
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Pergunte sobre nosso código de ética...")
    if prompt:
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user",  avatar="🤔"):
            st.write(prompt)

        with st.chat_message("assistant", avatar="😎"):
            with st.spinner("Buscando..."):
                answer = chain.invoke(prompt)
                st.write(answer)

        st.session_state["messages"].append({"role": "assistant", "content": answer})

