## Run the following installation if not done yet
# pip install langchain langchain-huggingface huggingface_hub python-dotenv pandas pydantic pdfplumber tk
###################################################################

import os
import tkinter as tk
from tkinter import filedialog

import pdfplumber
from dotenv import load_dotenv
from langchain.chains import LLMChain

# load apis
load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# load your resume path
def load_resume_local():
    root = tk.Tk()
    root.withdraw()
    pdf_path = filedialog.askopenfilename(
        title="Select Resume PDF",
        filetypes=[("PDF files", "*.pdf")]
    )
    root.destroy()
    if pdf_path:
        print(f"Resume Uploaded: {pdf_path}")
        return pdf_path
    else:
        print("Error: Mo file selected.")
        exit(1)

# Extract text from resume
def extract_from_pdf():
    while True:
        print("Uploading Resume...")
        path = load_resume_local()
        try:
            resume_text = ""
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text: resume_text += text + "\n"
            return resume_text
        except FileNotFoundError:
            print(f"Error: Path Not Found: {path}")
        except Exception as e:
            print(f"Error Occurred: {e}")

print(extract_from_pdf()[:1000])