import streamlit as st
from scraper.scraper import get_article
import summariser.hierarchical
from summariser import hierarchical

st.title("Web Article Summarizer")

url = st.text_input("Enter Web URL:")

if url:
    chunks = get_article(url)
    chunk_text = " ".join(chunks)
    st.subheader("Original Text")
    st.write(chunk_text)


    final_summary = hierarchical.multi_level_summary(chunks)
    st.subheader("Summary")
    st.write(final_summary)

    # text = get_article(url)
    # st.subheader("Original Text")
    # st.write(text)
    #
    # summary = get_summary(text)
    # st.subheader("Summary")
    # st.write(summary)

