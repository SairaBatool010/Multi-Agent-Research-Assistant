import sys
from pathlib import Path
import tempfile

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import streamlit as st

from app.run_research import generate_report

# RAG imports
from app.rag.document_loader import load_pdf
from app.rag.chunking import split_documents
from app.rag.embeddings import get_embeddings
from app.rag.vectordb import add_documents


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    layout="wide"
)

st.title("🧠 Multi-Agent Research Assistant")


# --------------------------------------------------
# PDF UPLOAD SECTION
# --------------------------------------------------

st.subheader("📄 Upload PDF Knowledge Base")

uploaded_file = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"]
)

if uploaded_file is not None:

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(uploaded_file.read())
            pdf_path = tmp.name

        with st.spinner("Processing PDF..."):

            # Load PDF
            docs = load_pdf(pdf_path)

            # Add source metadata
            for doc in docs:
                doc.metadata["source"] = uploaded_file.name

            # Split into chunks
            chunks = split_documents(docs)

            # Create embeddings
            embeddings = get_embeddings()

            # Store in ChromaDB
            add_documents(
                chunks,
                embeddings
            )

        st.success(
            f"PDF '{uploaded_file.name}' indexed successfully!"
        )

    except Exception as e:

        st.error(
            f"Failed to process PDF: {str(e)}"
        )


# --------------------------------------------------
# QUERY SECTION
# --------------------------------------------------

st.subheader("🔍 Research Query")

query = st.text_input(
    "Enter a research topic:"
)

report = ""


# --------------------------------------------------
# GENERATE REPORT
# --------------------------------------------------

if st.button("Generate Report"):

    if not query:

        st.warning(
            "Please enter a research topic."
        )

    else:

        with st.spinner("Researching..."):

            report = generate_report(query)

        st.success("Report generated!")

        st.markdown(report)


# --------------------------------------------------
# DOWNLOAD REPORT
# --------------------------------------------------

if report:

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="research_report.txt",
        mime="text/plain"
    )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("System Information")

    st.markdown("""
### Sources Available

✅ Internal PDF Documents (RAG)

✅ Web Search

✅ Wikipedia

✅ ArXiv

### Workflow

Planner Agent

⬇

Research Agent

⬇

Summarizer Agent

⬇

Fact Checker Agent

⬇

Writer Agent
""")