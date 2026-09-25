from typing import Dict, List
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import requests


def parse_science_news(page: int = 2) -> pd.DataFrame:
    """Parses science news articles from new-science.ru and extracts title, link, date, and views.

    Args:
        page (int): Target page number to scrape.

    Returns:
        pd.DataFrame: Structured dataset containing scraped news items.
    """
    url = f'https://new-science.ru/category/news/page/{page}/'
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/122.0.0.0 Safari/537.36'
        )
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    post_cards = soup.find_all('div', class_='post-details')

    news_data: Dict[str, List[str]] = {
        "news": [],
        "links": [],
        "views": [],
        "date": []
    }

    for post in post_cards:
        title_tag = post.find('h2', class_='post-title')
        link_tag = title_tag.find('a') if title_tag else None
        date_tag = post.find('span', class_='date meta-item tie-icon')
        views_tag = post.find('span', class_='meta-views meta-item')

        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        link = link_tag.get('href') if link_tag else "N/A"
        date = date_tag.get_text(strip=True) if date_tag else "N/A"
        views = views_tag.get_text(strip=True) if views_tag else "0"

        news_data["news"].append(title)
        news_data["links"].append(link)
        news_data["date"].append(date)
        news_data["views"].append(views)

    df_news = pd.DataFrame(news_data, columns=["news", "links", "views", "date"])
    return df_news


if __name__ == "__main__":
    try:
        df = parse_science_news(page=2)
        print(f"Scraped {len(df)} news items successfully:\n")
        print(df.head())

        # Optional export to CSV
        # df.to_csv("scraped_news.csv", index=False, encoding="utf-8-sig")

    except Exception as e:
        print(f"An error occurred during web scraping: {str(e)}")
