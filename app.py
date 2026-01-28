import streamlit as st
import tempfile

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

st.set_page_config(
    page_title="Chat with PDF",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Chat with PDF")
st.caption("Ask questions from your PDF using AI (RAG-based system)")



with st.sidebar:
    st.header("ℹ️ How it works")
    st.markdown("""
    1. Upload a PDF  
    2. The document is split into chunks  
    3. Relevant content is retrieved  
    4. AI answers **only from the PDF**
    """)
    st.markdown("---")
    st.markdown("🛡️ **Hallucination Control**  \nIf answer is not present, AI will say *Not found in document*.")



uploaded_file = st.file_uploader("📤 Upload a PDF file", type="pdf")

if uploaded_file is not None:
    st.success(f"✅ Uploaded: **{uploaded_file.name}**")

    with st.spinner("📖 Reading and processing PDF..."):
        # save pdf temporarily
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name

        # load pdf
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        # split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = splitter.split_documents(documents)

        # embeddings + vector store
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_documents(chunks, embeddings)

        # LLM
        llm = ChatOpenAI(temperature=0)
        retriever = vectorstore.as_retriever()

        # prompt
        template = """
        Answer the question using ONLY the context below.
        If the answer is not present, say "Answer not found in the document".

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=template
        )

        def get_answer(question):
            docs = retriever.get_relevant_documents(question)
            context = "\n\n".join([doc.page_content for doc in docs])
            return llm.predict(
                prompt.format(context=context, question=question)
            )

    st.markdown("---")

    
    query = st.text_input("❓ Ask a question from the PDF")

    if query:
        with st.spinner("🤖 Thinking..."):
            answer = get_answer(query)

        st.markdown("### 📌 Answer")
        st.info(answer)
