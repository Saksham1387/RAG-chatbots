from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama

loader = DirectoryLoader('pdfs', glob="*.pdf", show_progress=True)
docs = loader.load()
print(docs)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
text_splitter.split_documents(docs)[:5]

documents=text_splitter.split_documents(docs)
print(documents)

db=FAISS.from_documents(documents[:30],OllamaEmbeddings())
print(db)

query="An attention function can be described as mapping a query "
result=db.similarity_search(query)
print("                       -----------------------------------------------------                           ")
print("Result of the query:  ")
print(result[0].page_content)


## Load Ollama LAMA2 LLM model
llm=Ollama(model="llama2")
print(llm)