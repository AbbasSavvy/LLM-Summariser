import time
from summariser.llm_summary import get_summary

def summarize_chunks_safely(chunks, delay: float = 1.5):
    summaries = []
    for i, chunk in enumerate(chunks):
        try:
            summary = get_summary(chunk)
            summaries.append(summary)
            print(f"Chunk {i+1}/{len(chunks)} summarized.")
        except Exception as e:
            print(f"Error summarizing chunk {i+1}: {e}")
        time.sleep(delay) 
    return summaries

def hierarchical_summary_safe(chunks, delay: float = 1.5):
    chunk_summaries = summarize_chunks_safely(chunks, delay)
    combined_input = " ".join(chunk_summaries)
    return combined_input
