from langchain.text_splitter import RecursiveCharacterTextSplitter
import requests
from bs4 import BeautifulSoup
import re

def get_article(url: str, chunk_size: int = 1500,  chunk_overlap: int = 150):
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
    # paragraphs = soup.find_all("p")
    # text = " ".join([p.get_text() for p in paragraphs])

    # 1. Look for a semantic <main> or <article> tag
    article_container = soup.find(["main", "article"])

    # 2. If not found, look for common article-related IDs or classes
    if not article_container:
        article_container = soup.find(
            lambda tag: tag.name in ["div", "section"] and
                        any(
                            re.search(r'article|post|main|content|story', c, re.I) for c in tag.get('class', [])
                        )
        )

    # 3. If a container is found, get all the paragraphs inside it
    if article_container:
        paragraphs = article_container.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])
    else:
        # 4. Fallback: If no specific container is found, get all paragraphs on the page
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_text(text)

    return chunks

