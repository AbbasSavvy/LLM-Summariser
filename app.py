import streamlit as st
from scraper.scraper import get_article
from summariser.llm_summary import get_summary

st.title("Web Article Summarizer")

url = st.text_input("Enter Web URL:")

if url:
    article_text = get_article(url)
    summary = get_summary(article_text)
    st.subheader("Summary")
    st.write(summary)



