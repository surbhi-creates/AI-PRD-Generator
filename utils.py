import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompt import PRD_PROMPT_TEMPLATE  # your existing prompt import

# Load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model (gemini-3.5-flash is fast and free-tier friendly)
model = genai.GenerativeModel('gemini-3.5-flash')

def generate_prd(product_details: str) -> str:
    """
    Takes product details from the user,
    combines with the PRD prompt template,
    and returns the generated PRD text.
    """
    try:
        # Combine your prompt template with user input
        full_prompt = PRD_PROMPT_TEMPLATE.format(product_details=product_details)
        
        # Generate content
        response = model.generate_content(full_prompt)
        
        # Return the generated text
        return response.text

    except Exception as e:
        return f"❌ Error generating PRD: {str(e)}"