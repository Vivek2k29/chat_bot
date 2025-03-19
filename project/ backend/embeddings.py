from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def create_vector_store(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAISS.from_documents(texts, embeddings)

    vectorstore.save_local("faiss_index")
    return vectorstore


if __name__ == "__main__":
    from loader.py import load_website_data

    url = "https://brainlox.com/courses/category/technical"
    docs = load_website_data(url)
    vectorstore = create_vector_store(docs)
    print("Vector store created successfully.")
