import cohere
import os
from dotenv import load_dotenv
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_design_brief(
    design_type: str,
    industry: str,
    difficulty: str,
    brief_type: str,
    include_branding: bool = True,
    include_user_story: bool = True
) -> str:
    """
    Generate a professional design brief using Cohere's chat API.
    """

    prompt = f"""
Generate a professional {brief_type.lower()} {design_type.upper()} design brief 
for a project in the {industry} industry.
The project difficulty should be {difficulty.lower()}.

The output MUST use Markdown with the following structure:
# [Brand Name]

## Project Overview
[overview text]

## Project Goals
[goals]

## Branding Guidelines
[brand name]
[5-6 HEX colors]

## Deliverables
[list]

## User Stories
(at least 2–3, in the format: 
"As a [user type], I want to [action], so that [goal].")

Keep it concise, clear, and professional. No emojis.
"""


    response = co.chat(
        model="command-r-plus",
        message=prompt,
        temperature=0.7,
        max_tokens=500
    )

    return response.text.strip()