from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("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")


def get_chat_response(query):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAISS.load_local("faiss_index", embeddings)

    llm = ChatOpenAI(temperature=0.5, openai_api_key=OPENAI_API_KEY)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectorstore.as_retriever())

    return qa_chain.run(query)


if __name__ == "__main__":
    query = "What courses are available?"
    response = get_chat_response(query)
    print("Chatbot Response:", response)
