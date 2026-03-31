import os
from dotenv import load_dotenv
from google import genai
import json
import jsonify
from processor import processed

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """You are an expert code reviewer. Analyze the provided code and return a JSON response with this exact structure:
{
    "what_it_does": "A one paragraph plain-English description of the project",
    "tech_stack_summary": "Built with Python and Flask...",
    "structure_overview": "The project is organised into 3 main modules..."
}
Return ONLY valid JSON. No markdown, no extra text."""


def summarize():
    data = processed()

    prompt = SYSTEM_PROMPT
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    raw = response.text.strip()
    if raw.startswith("```"):
            raw = raw.split("\n", 1)[1]
            raw = raw.rsplit("```", 1)[0]

    result = json.loads(raw)
    return jsonify(result)


def gen_arch_diagram():
    pass


def file_explanantion():
    pass

def codebase():
    pass

