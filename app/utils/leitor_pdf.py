from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# logica do contexto do RAG
def carregar_pdf():  # ler o pdf e extrair o texto do pdf
    pdf_loader = PyPDFLoader("docs/etica_banco.pdf")
    texto = pdf_loader.load()
    return texto

def separar_em_blocos(texto_pdf):
    separador = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    lista_blocos = separador.split_documents(texto_pdf)
    return lista_blocos

