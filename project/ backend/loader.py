from langchain.document_loaders import WebBaseLoader

def load_website_data(url):
    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents

if __name__ == "__main__":
    url = "https://brainlox.com/courses/category/technical"
    docs = load_website_data(url)
    print(docs)
