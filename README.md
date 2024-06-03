
# Retrieval-Augmented Generation

This Repo consist of three ways to implement a RAG architecture.This is a part of implementing a Chat-bot for my project Bhasha-Buddy
GitHub: https://github.com/Saksham1387/Bhasha-Buddy.git

## 1. Simple 
This is the retrivel.ipynb.This notebook consist of code for making a chatbot using a Llama-2 7B model, running locally on your machine using Ollama.The dataset was tested with was a text file contaning multiple dairy entries of people suffering from Stuttering.
The responses were pretty good.

## 2. Muliple files using Llama Index
This the Rag-multiple.ipynb.This notebook consists of code for implementing a chatbot using multiple PDFs and indexing them using Llama-index.

## 3. Graph-RAGs
This is the Rag-graph.ipynb.This notebook the implementation of a chatbot with a Graph database Neo4j, you have to provide your APIs for that.Using Graphs in here increases the Retrieval speed.

## How to Run?
Running all of these notebooks is very easy.

1. Create a Virtual Enviornment 
2. Run 
```python
pip install -r requirements.txt