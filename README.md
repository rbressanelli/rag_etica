# Projeto Agente RAG

## O que é um agente RAG?
Um agente RAG (Retrieval-Augmented Generation ou Geração Aumentada por Recuperação) é um sistema de Inteligência Artificial. Ele combina a geração de texto dos Grandes Modelos de Linguagem (LLMs, como GPT-4, Gemini) com a capacidade de buscar informações externas e atualizadas em tempo real. <br>

Um agente RAG difere de um LLM tradicional. O agente RAG consulta uma base de conhecimento confiável (documentos, PDFs, bancos de dados). Ele responde a perguntas com precisão, o que reduz as "alucinações" (invenções).

## Requisitos
Necessário ter o Python 3.13+ instalado

## Rodar a aplicação
- Clonar o repositório
- Criar o ambiente virtual e ativá-lo
- Instalar os pacotes de dependências
- Renomear o arquivo .env.example para .env
- Incluir sua chave da OpenAI como valor da variável do .env
- Rodar a aplicação com o seguinte comando: <b>streamlit run app/main.py</b>
- Será aberta uma janela (ou aba) em seu navegador com o chat esperando as perguntas

## Informações adicionais

O chat se baseia no documento em anexo <i>etica_banco</i> que simula um código de ética de um banco fictício. O documento foi gerado por IA e tenta se aproximar de uma situação real.<br>
Existe outro documento em anexo que pode ser utilizado como teste, caso ache necessário.

### Créditos
Projeto baseado em um projeto realizado pela #hashtagprogramação 



