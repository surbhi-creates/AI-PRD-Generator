# 🧠 AI PRD Generator — Portfolio Case Study

## 1. The Problem
Writing a professional Product Requirements Document (PRD) manually takes 3–4 hours. Product managers, founders, and designers often struggle with:
- Structuring the document correctly
- Remembering all sections (user stories, KPIs, timelines, etc.)
- Formatting and consistency

## 2. The Solution
I built an **AI PRD Generator** that creates a complete, structured PRD in under 30 seconds. Users simply enter:
- Problem Statement
- Target User
- Product Context

And the AI generates a professional PRD with 10 sections.

## 3. Live Demo
🔗 [https://ai-prd-generator-surbhi-creates.streamlit.app]

## 4. GitHub Repository
🔗 [https://github.com/surbhi-creates/AI-PRD-Generator]

## 5. Tech Stack
| Technology | Purpose |
|-----------|---------|
| **Python** | Backend logic |
| **Streamlit** | Frontend web interface |
| **Google Gemini API** | AI engine for PRD generation |
| **FPDF** | PDF export functionality |

## 6. Key Features
- ✅ **10-section PRD generation**: Executive Summary, Problem Statement, Target Audience, User Stories, Functional Requirements, Non-Functional Requirements, KPIs, Timeline, Risks, Appendix
- ✅ **One-click export**: Download as Markdown or PDF
- ✅ **Modular architecture**: Swapped from Claude to Gemini seamlessly when API credits ran out
- ✅ **Real-world validation**: Generated sample PRDs for WhatsApp, Zepto, and PhonePe

## 7. My Role & Learnings
**Solo builder** — handled everything from product ideation to deployment.

**Key learnings:**
- **Prompt engineering**: Crafting structured prompts to get consistent AI output
- **API integration**: Working with LLM APIs and handling errors gracefully
- **Modular design**: Building provider-agnostic code so any LLM can be swapped in
- **Deployment**: Shipping a live app on Streamlit Cloud

## 8. Architecture Diagram
User Input (Streamlit UI)
↓
Google Gemini API (AI Generation)
↓
Structured PRD Output
↓
Export to Markdown / PDF

## 9. Future Roadmap
- [ ] Add support for OpenAI GPT and Groq
- [ ] User authentication & saved PRD history
- [ ] Custom PRD templates (Lean Canvas, BRD, etc.)
- [ ] Team collaboration features

---

**Built with ❤️ by Surbhi**
