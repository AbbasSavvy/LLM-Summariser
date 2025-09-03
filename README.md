# Web Article Summarizer

This is a Python-based web application that scrapes the content of a web article from a given URL and generates a concise summary using a Large Language Model (LLM). The application uses a hierarchical summarization approach to handle long articles that exceed the LLM's token limit.

## Features

- **Web Scraping:** Scrapes text from web pages, focusing on the main article content.
- **Hierarchical Summarization:** Efficiently summarizes articles of any length by breaking them into chunks, summarizing each chunk, and then creating a final summary of those summaries.
- **Interactive Interface:** A simple web interface built with Streamlit for easy use.
- **Robustness:** Includes error handling for web scraping and LLM API calls, along with rate-limiting to prevent API issues.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+

You will also need an **API token** from Hugging Face to use their models.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/AbbasSavvy/web-llm-summariser.git](https://github.com/AbbasSavvy/web-llm-summariser.git)
    cd web-llm-summariser
    ```

2.  **Create and activate a virtual environment:**
    It is recommended to use a virtual environment to manage project dependencies.
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3.  **Install the dependencies:**
    The `requirements.txt` file lists all the necessary libraries for this project.
    ```bash
    pip install -r requirements.txt
    ```
    
---

## Configuration

1.  **Set up your API token:**
    Create a file named `.env` in the root directory of the project.
    Inside this file, add your Hugging Face API token:
    ```
    HUGGINGFACEHUB_API_TOKEN="YOUR_API_KEY_HERE"
    ```
    Replace `"YOUR_API_KEY_HERE"` with the actual token you obtained from Hugging Face.

---

## How to Run

1.  **Ensure your virtual environment is active.**

2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

This command will start a local web server and open the application in your default web browser. You can then enter a web article URL in the provided text box to generate a summary.