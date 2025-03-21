# 🧠 LangChain Custom Chatbot  

A Flask-based chatbot that extracts course data from [Brainlox Technical Courses](https://brainlox.com/courses/category/technical), processes it using embeddings, and provides intelligent responses via a RESTful API.  

## 🚀 Features  
- ✅ **Web Scraping**: Uses LangChain URL Loaders & BeautifulSoup to extract data.  
- ✅ **Embeddings Generation**: Converts extracted text into vector embeddings using OpenAI/Hugging Face models.  
- ✅ **Vector Database Storage**: Stores embeddings in FAISS/ChromaDB for efficient retrieval.  
- ✅ **Flask RESTful API**: Provides an endpoint for chatbot interactions.  
- ✅ **LLM-based Response Generation**: Uses a language model to provide relevant responses.  
- ✅ **Modular Code Structure**: Clean separation for data extraction, vector processing, and API handling.  

## 🛠️ Tech Stack  
- **Backend**: Flask, LangChain  
- **Vector Store**: FAISS / ChromaDB  
- **Embeddings**: OpenAI / Hugging Face  
- **Web Scraping**: BeautifulSoup, Requests  
- **API Framework**: Flask-RESTful  

## 📌 Setup Instructions  
1️⃣ **Clone the Repository**:  
```bash
git clone https://github.com/Vivek2k29/chat_bot.git
cd chat_bot
