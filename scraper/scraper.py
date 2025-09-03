from langchain.text_splitter import CharacterTextSplitter
import requests
from bs4 import BeautifulSoup

def get_article(url: str, chunk_size: int = 500,  chunk_overlap: int = 50):
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

    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_text(text)

    return chunks

