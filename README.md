# Chat with PDF using LLM and RAG

## Problem
Reading long PDF documents manually is time-consuming.

## Solution
This application allows users to upload a PDF and ask questions.
It uses Retrieval Augmented Generation (RAG) to ensure answers
are based only on document content.

## Architecture
1. PDF upload
2. Text extraction
3. Chunking
4. Embeddings generation
5. Vector database (FAISS)
6. LLM-based answer generation

## Hallucination Control
The model is restricted to answer only from the document.
If information is not found, it avoids guessing.

## Advanced Feature
Supports querying across multiple PDFs.

## Limitations
Large PDFs may slow down response time.

## Challenges Faced & Solutions

During development, the following issues were encountered:

### 1. LangChain Import Errors
- Issue: Modules like `langchain.document_loaders` and `langchain.text_splitter` caused errors due to version changes.
- Solution: Updated imports to use `langchain-community`, `langchain-text-splitters`, and `langchain-openai` packages.

### 2. Deprecated RetrievalQA Chain
- Issue: `RetrievalQA` chain caused compatibility issues with newer LangChain versions.
- Solution: Implemented a custom retriever + prompt-based QA approach for better stability and control.

### 3. Streamlit Command Not Found
- Issue: `streamlit run app.py` was not recognized on Windows.
- Solution: Used `python -m streamlit run app.py` to correctly execute Streamlit.

### 4. OpenAI API Key Error
- Issue: Application failed due to missing or invalid OpenAI API key.
- Solution: Clearly documented API key requirement in README. The key is intentionally not included for security and billing reasons.

These issues reflect real-world development challenges and were resolved using debugging and dependency management best practices.
