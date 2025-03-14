import datetime
import requests
from app.config import GNEWS_API_KEY  

GNEWS_BASE_URL = "https://gnews.io/api/v4/search"

def fetch_news(preferences, past_days=1):
    today=datetime.datetime.today()
    from_date=today - datetime.timedelta(days=past_days)

    news_results=[]

    for topic in preferences:
        params = {
            "q": topic,
            "from": from_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "lang": "en",
            "max": 5,  # Fetch top 5 articles per topic
            "token": GNEWS_API_KEY
        }

        try:
            response=requests.get(GNEWS_BASE_URL, params=params)
            data=response.json()
            #print(f"Raw API Response for '{topic}': {data}")  # Debugging

            if "articles" in data and data["articles"]:
                news_results.extend(data["articles"][:5])  
            else:
                print(f"No articles found for '{topic}'")

        except Exception as e:
            print(f"Error fetching news for '{topic}': {e}")

    return news_results
