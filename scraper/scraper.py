import requests
from bs4 import BeautifulSoup

def get_article(url: str, max_chars: int = 2000) -> str:
    """
    Scrape all paragraphs from a webpage and return as a single string.
    Limits the text to max_chars for LLM input.
    """
    response = requests.get(url)

    # Ensure request was successful
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = " ".join([p.get_text() for p in paragraphs])

    return text[:max_chars]
