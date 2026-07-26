PRD_PROMPT_TEMPLATE = """You are an expert Product Manager with 10+ years of experience building successful tech products.

Use the following information provided by the user:

Problem Statement:
{problem_statement}

Target User:
{target_user}

Product Context:
{product_context}

Create the PRD in Markdown format.

Structure the PRD with the following sections:

# 1. Executive Summary
Brief overview of the product and its purpose.

# 2. Problem Statement
What problem does this product solve? Why does it matter?

# 3. Target Audience & User Personas
Who are the primary users? Include 2-3 user personas.

# 4. User Stories
List 5-7 user stories in "As a [user], I want [goal], so that [benefit]" format.

# 5. Functional Requirements
Detailed list of features and capabilities.

# 6. Non-Functional Requirements
Performance, security, scalability, and usability requirements.

# 7. Success Metrics (KPIs)
How will we measure success? Include specific metrics.

# 8. Timeline & Milestones
Suggested development phases and timeline.

# 9. Risks & Mitigations
Potential risks and how to address them.

# 10. Appendix
Any additional notes, references, or diagrams.

Use bullet points, tables, and clear headings. Be specific and actionable.
"""