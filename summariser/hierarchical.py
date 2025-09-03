import time

from langchain_text_splitters import RecursiveCharacterTextSplitter

from summariser.llm_summary import get_summary, get_final_summ
import streamlit as st

def summarize_chunks_safely(chunks, delay: float = 1.5, final_flag=False):

    if not final_flag:

        summaries = []

        # Create a progress bar and status text
        progress_bar = st.progress(0, text="Summarizing chunks...")
        status_text = st.empty()

        for i, chunk in enumerate(chunks):
            try:
                status_text.write(f"Summarizing chunk {i + 1} of {len(chunks)}...")
                summary = get_summary(chunk)
                summaries.append(summary)

                progress_bar.progress((i + 1) / len(chunks))

            except Exception as e:
                print(f"Error summarizing chunk {i+1}: {e}")
            # time.sleep(delay)


        status_text.write("Chunk summarization complete.")
        progress_bar.empty()

        return summaries

    else:
        summaries = []

        # Create a progress bar and status text
        progress_bar = st.progress(0, text="Summarizing chunks...")
        status_text = st.empty()

        for i, chunk in enumerate(chunks):
            try:
                status_text.write(f"Summarizing chunk {i + 1} of {len(chunks)}...")
                summary = get_final_summ(chunk)
                summaries.append(summary)

                progress_bar.progress((i + 1) / len(chunks))

            except Exception as e:
                print(f"Error summarizing chunk {i + 1}: {e}")
            # time.sleep(delay)

        status_text.write("Chunk summarization complete.")
        progress_bar.empty()

        return summaries


def hierarchical_summary_safe(chunks, delay: float = 1.5):
    chunk_summaries = summarize_chunks_safely(chunks, delay)
    combined_input = " ".join(chunk_summaries)
    return combined_input


def multi_level_summary(chunks, chunk_size: int = 1000, chunk_overlap: int = 100):
    st.subheader("Summarizing chunks...")
    chunk_summaries = summarize_chunks_safely(chunks, delay=1)


    combined_summaries = " ".join(chunk_summaries)


    summary_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    final_chunks = summary_splitter.split_text(combined_summaries)


    st.subheader("Generating Final Summary...")
    final_summaries = summarize_chunks_safely(final_chunks, delay=1, final_flag=True)


    return " ".join(final_summaries)