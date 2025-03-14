import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def summarize_news(articles):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = "\n\n".join([f"Summarize this in 4-5 sentences: {article['title']} - {article['content']}" for article in articles])
    response = model.generate_content(prompt)
    return response.text.strip().split("\n\n")  # Split summaries for each article


def score_news(article, user_preferences):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    Given the user preferences {user_preferences}, score the following news article on a scale of 1-100 based on relevance.
    Title: {article['title']}
    Content: {article['content']}
    please output only integer value.
    """
    response = model.generate_content(prompt)
    try:
        score = int(response.text.strip())
    except ValueError:
        score = 50  # Default score if parsing fails
    return score
