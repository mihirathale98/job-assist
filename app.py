import streamlit as st
import PyPDF2
from src.models import TogetherModel

model = TogetherModel()

# Streamlit file uploader
st.title("PDF Uploader using PyPDF2")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    
    # Get number of pages
    num_pages = len(pdf_reader.pages)
    st.write(f"Number of pages: {num_pages}")
    
    # Extract and display text from each page
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        st.write(f"### Page {page_num + 1}")
        st.write(text)
