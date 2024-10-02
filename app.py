import streamlit as st
import PyPDF2
from src.process_resume import preprocess_resume
# Streamlit file uploader
st.title("PDF Uploader using PyPDF2")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    
    # Get number of pages
    num_pages = len(pdf_reader.pages)
    st.write(f"Number of pages: {num_pages}")
    all_text = ""
    # Extract and display text from each page
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        all_text += text

    with st.spinner("Preprocessing..."):
        markdown_resume = preprocess_resume(all_text)

    st.markdown(markdown_resume)

    


