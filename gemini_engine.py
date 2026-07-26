import os
import google.generativeai as genai
from dotenv import load_dotenv
from fpdf import FPDF
from prd_prompt import PRD_PROMPT_TEMPLATE

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash')

def generate_prd(problem_statement, target_user, product_context):
    try:
        full_prompt = PRD_PROMPT_TEMPLATE.format(
            problem_statement=problem_statement,
            target_user=target_user,
            product_context=product_context
        )
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

def save_as_markdown(prd_text: str, filename: str = "PRD.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(prd_text)
    return filename

def save_as_pdf(prd_text: str, filename: str = "PRD.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=8)
    
    clean_text = prd_text.encode('latin-1', 'replace').decode('latin-1')
    
    for line in clean_text.split("\n"):
        line = line.replace('\t', '    ').rstrip()
        
        if not line:
            pdf.ln(3)
            continue
        
        # BULLETPROOF: try to write the line. If ANY error, skip it.
        try:
            pdf.cell(0, 4, txt=line, ln=1)
        except Exception:
            try:
                # If full line fails, write first 70 chars only
                pdf.cell(0, 4, txt=line[:70], ln=1)
            except Exception:
                # Absolute last resort: skip this line entirely
                pdf.cell(0, 4, txt="[...]", ln=1)
    
    pdf.output(filename)
    return filename
