from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI

db = FAISS.load_local("index/faiss", OpenAIEmbeddings())
llm = ChatOpenAI(model="gpt-4o-mini")

def answer(question: str) -> str:
    docs = db.similarity_search(question, k=5)
    ctx = "\n\n".join(d.page_content for d in docs)
    prompt = open('prompts/developer_system.txt').read()
    return llm.predict(f"{prompt}\n\nКонтекст:\n{ctx}\n\nВопрос: {question}")
