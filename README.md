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
