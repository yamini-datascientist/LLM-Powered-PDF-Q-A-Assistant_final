import streamlit as st
import tempfile
import os
from dotenv import load_dotenv
from ingest import PDFIngestor
from qa_chain import QAChain

load_dotenv()

st.set_page_config(page_title="PDF Q&A Assistant", page_icon="🤖")
st.title("📄 LLM-Powered PDF Q&A Assistant")

if "ingestor" not in st.session_state:
    st.session_state.ingestor = None

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = QAChain()

uploaded_files = st.file_uploader(
    "Upload one or more PDF documents", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("Processing PDFs and building index..."):
        temp_paths = []
        for pdf_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(pdf_file.getbuffer())
                temp_paths.append(tmp.name)

        ingestor = PDFIngestor()
        ingestor.ingest(temp_paths)
        st.session_state.ingestor = ingestor

        # Clean up temp files
        for path in temp_paths:
            os.unlink(path)

        st.success(f"Processed {len(uploaded_files)} PDFs and built vector index!")
else:
    st.info("Upload PDFs to get started.")

question = st.text_input("Ask a question about the uploaded PDFs:")

if st.button("Get Answer") and question:
    if st.session_state.ingestor is None:
        st.warning("Please upload and process PDFs first.")
    else:
        with st.spinner("Retrieving answer..."):
            relevant_chunks = st.session_state.ingestor.search(question, top_k=5)
            answer = st.session_state.qa_chain.generate_answer(question, relevant_chunks)

            st.markdown("### 📝 Answer:")
            st.write(answer)

            with st.expander("Retrieved Context Passages"):
                for i, chunk in enumerate(relevant_chunks, 1):
                    st.markdown(f"**Passage {i}:**")
                    st.write(chunk)
else:
    st.info("Enter a question and click 'Get Answer'.")
