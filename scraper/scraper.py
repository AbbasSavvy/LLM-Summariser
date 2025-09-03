import requests
from bs4 import BeautifulSoup

def get_article(url: str, max_chars: int = 20000) -> str:
    """
    Scrape all paragraphs from a webpage and return as a single string.
    Limits the text to max_chars for LLM input.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/139.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    # Ensure request was successful
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = " ".join([p.get_text() for p in paragraphs])

    return text[:max_chars]
