# Techin-lab-6

It is an improvisation on lab5, A simple web app to generate and download cover letter from the uploaded resume and entered job description and company using Gemini API and Streamlit.  

By providing the example cover letter in the prompt, the language model can better understand the desired structure, tone, and content for generating a high-quality cover letter. This technique can help improve the relevance, coherence, and personalization of the generated cover letter.
Features of the Cover Letter Generator Application:
1.Resume Upload: The application allows users to upload their resume in PDF format, which is then parsed to extract the text content.
2.Job Description Input: Users can enter the job description for the position they are applying for.
3.Company Name Input: Users can specify the company name for which they are generating the cover letter.
4.Example Cover Letter Editing: Users can edit or replace a default example cover letter, which is then used in the few-shot learning prompt.
5.Cover Letter Generation: After providing the necessary inputs (resume, job description, company name, and example cover letter), users can click a button to generate a new cover letter tailored to their specific application.
6.Cover Letter Display: The generated cover letter is displayed on the application interface for the user to review.
7.PDF Download: Users can download the generated cover letter as a PDF file for submission or printing.

## How to Run
Open the terminal and run the following commands:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
Or just go the link : [Cover Letter Generator](https://techin-lab5-coverlettergenerator.streamlit.app/)

## What's Included

- `app.py`: The main application made with streamlit.

## Lessons Learned

- How to make use Gemini API's for a pre defined task.
- How to use chat box feature in streamlit.
- How to create upload file feature in streamlit and do OCR of uploaded PDF file.
