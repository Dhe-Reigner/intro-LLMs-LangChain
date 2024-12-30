import PyPDF2
import streamlit as st

import os

pdf_path = "docs/Desktop/17 Sustainable Development Goals: United Nations – Global Rewilding Initiative: Rewilding People & Nature.pdf"

if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        print("Total number of characters:", len(text))
        print("Preview of the text:", text[:99])
else:
    print("File not found. Please check the path.")
