import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from os import getenv
import base64
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import io

load_dotenv()
genai.configure(api_key=getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def generate_cover_letter(resume_text, job_description, company_name):
    prompt = f"Generate a cover letter based on the following resume:\n\n{resume_text}\n\nfor the following job description at {company_name}:\n\n{job_description}"
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("Cover Letter Generator")

    if 'resume_text' not in st.session_state:
        st.session_state.resume_text = None
    if 'cover_letter' not in st.session_state:
        st.session_state.cover_letter = None

    uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
    if uploaded_file is not None:
        st.success("Resume Uploaded Successfully!")
        resume_text = extract_text_from_pdf(uploaded_file)
        st.session_state.resume_text = resume_text

    company_name = st.text_input("Enter company name:")
    job_description = st.text_area("Enter job description:")

    if st.button("Generate Cover Letter"):
        with st.spinner("Your cover letter is being generated!! Hang Tight!"):
            if st.session_state.resume_text is not None and job_description and company_name:
                cover_letter = generate_cover_letter(st.session_state.resume_text, job_description, company_name)
                st.session_state.cover_letter = cover_letter
                st.write("Generated Cover Letter:")
                st.write(cover_letter)

    if st.session_state.cover_letter is not None:
        styles = getSampleStyleSheet()
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []
        text = Paragraph(st.session_state.cover_letter, styles["BodyText"])
        elements.append(text)
        doc.build(elements)

        base64_pdf = base64.b64encode(buffer.getvalue()).decode('utf-8')
        href = f'<a href="data:application/pdf;base64,{base64_pdf}" download="cover_letter.pdf" target="_blank">Download Cover Letter as PDF</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()