import schedule
import time
from app import users_collection
from app.news_fetcher import fetch_news
from app.news_processor import summarize_news, score_news
from app.email_sender import generate_news_digest

def daily_news_job():
    users = users_collection.find()
    
    for user in users:
        email = user["email"]
        preferences = user["preferences"]
        articles = fetch_news(preferences)

        if not articles:
            print(f"⚠️ No articles found for {email}")
            continue

        #  Batch summarize all articles in a single API call
        summaries = summarize_news(articles)  

        # Score articles efficiently
        processed_articles = []
        for article, summary in zip(articles, summaries):
            score = score_news(article, preferences)  # Calls Gemini once per article
            processed_articles.append({
                "title": article["title"],
                "summary": summary,
                "url": article["url"],
                "score": score
            })

        # Sort by score & send top 5 articles
        processed_articles.sort(key=lambda x: x["score"], reverse=True)
        top_articles = processed_articles[:5]

        generate_news_digest(email, preferences, top_articles)
        print(f"📩 Email sent to {email}")
daily_news_job()
# Schedule job at 8:23 AM
schedule.every().day.at("13:06").do(daily_news_job)

def run_scheduler():
    print("✅ News email scheduler running...")
    while True:
        
        schedule.run_pending()
        time.sleep(30)  # Check every 30 seconds

run_scheduler()