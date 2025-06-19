"""Agente conversacional de ejemplo usando RAG con LangChain y GPT-4o mini."""

import os
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv


def load_documents(path: str):
    """Carga documentos de texto plano desde el path indicado."""
    loader = TextLoader(path, encoding="utf-8")
    return loader.load()


def build_vectorstore(docs, persist_directory: str = "db"):
    """Construye o carga una base de vectores persistente."""
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)
    vectorstore.persist()
    return vectorstore


def main():
    load_dotenv()
    documents = load_documents("manual_servicio.txt")
    store = build_vectorstore(documents)

    llm = OpenAI(model="gpt-4o", temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=store.as_retriever())

    print("Agente conversacional listo. Escribe 'salir' para terminar.")
    while True:
        question = input("Usuario: ")
        if question.lower() == "salir":
            break
        answer = qa.run(question)
        print(f"Agente: {answer}\n")


if __name__ == "__main__":
    main()
