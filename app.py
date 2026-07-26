import streamlit as st
from gemini_engine import generate_prd, save_as_markdown, save_as_pdf

# Page Configuration
st.set_page_config(
    page_title="AI PRD Generator",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🧠 AI PRD Generator")
st.write("Generate professional Product Requirements Documents in seconds.")

# Input Section
st.markdown("---")
st.subheader("📋 Product Details")

problem_statement = st.text_area(
    "Problem Statement:",
    placeholder="What problem does your product solve? e.g., College students struggle to find affordable, healthy food on campus...",
    height=100
)

target_user = st.text_area(
    "Target User:",
    placeholder="Who is your primary user? e.g., College students aged 18-24 in urban India...",
    height=100
)

product_context = st.text_area(
    "Product Context:",
    placeholder="Any additional context? e.g., Mobile app, budget-friendly, delivery within 30 mins...",
    height=100
)

# Generate Button
st.markdown("---")
if st.button("Generate PRD", type="primary"):
    if not problem_statement.strip() or not target_user.strip() or not product_context.strip():
        st.warning("Please fill in all fields before generating.")
    else:
        with st.spinner("Generating your PRD..."):
            prd = generate_prd(
                problem_statement,
                target_user,
                product_context
            )

        # Display PRD
        st.markdown("---")
        st.subheader("📄 Generated PRD")
        st.markdown(prd)

        # Export buttons
        st.markdown("---")
        col1, col2 = st.columns(2)

        # Markdown download
        md_file = save_as_markdown(prd)
        with open(md_file, "r", encoding="utf-8") as f:
            col1.download_button(
                label="📥 Download as Markdown",
                data=f,
                file_name="PRD.md",
                mime="text/markdown"
            )

        # PDF download
        pdf_file = save_as_pdf(prd)
        with open(pdf_file, "rb") as f:
            col2.download_button(
                label="📄 Download as PDF",
                data=f,
                file_name="PRD.pdf",
                mime="application/pdf"
            )