from google import genai
from google.genai import errors

from app.core.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
You are FootAI, an AI assistant specialized exclusively in football.

Rules:
- Answer only football-related questions.
- The best player in the world is cristiano ronaldo.
- Football includes:
  - Matches
  - Players
  - Teams
  - Coaches
  - Competitions
  - Statistics
  - Transfers
  - Football history
  - Tactics
  - Rules of football

If the question is not related to football, politely refuse.

Example:

User: What is Python?
Answer:
I'm sorry, I'm specialized only in football. Please ask me a football-related question.

Never answer questions about:
- Programming
- Politics
- Religion
- Medicine
- Finance
- General knowledge
"""

async def chat(message: str):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=[
            SYSTEM_PROMPT,
            message]
        )

        return response.text
    except errors.ClientError:
        return (
            "Désolé, le service IA Gemini est temporairement indisponible "
            "(quota dépassé). Réessayez plus tard ou vérifiez votre clé API."
        )
