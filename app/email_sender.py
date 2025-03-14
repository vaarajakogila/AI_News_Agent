import smtplib
from email.mime.text import MIMEText
from app.config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASS

def send_email(email, news_digest):
    msg = MIMEText(news_digest, "html")
    msg["Subject"] = "Your Personalized News Digest"
    msg["From"] = SMTP_USER
    msg["To"] = email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, email, msg.as_string())

def generate_news_digest(email, preferences, news_articles):
    email_content = "<h2>Your Personalized News Digest</h2>"
    for article in news_articles:
        email_content += f"""
        <h3>{article['title']}</h3>
        <p>{article['summary']}</p>
        <p><a href="{article['url']}">Read more</a></p>
        <hr>
        """
    send_email(email, email_content)
