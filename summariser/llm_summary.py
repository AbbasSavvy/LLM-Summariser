import os
from pathlib import Path
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


project_root = Path(__file__).parent.parent
dotenv_path = project_root / ".env"

if dotenv_path.exists():
    load_dotenv(dotenv_path)
else:
    print("Warning: .env file not found at project root. Make sure your token is set!")


HF_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not HF_API_KEY:
    raise ValueError(
        "Hugging Face API token not found! "
        "Add HUGGINGFACEHUB_API_TOKEN to your .env file or environment variables."
    )


llm = HuggingFaceHub(
    repo_id="google/flan-t5-small",  # free model
    model_kwargs={"temperature": 0, "max_length": 300},
    huggingfacehub_api_token=HF_API_KEY,
    task="summarization"
)

template = """Summarize the following article in 3-5 sentences:

{text}

Summary:"""

prompt = PromptTemplate(template=template, input_variables=["text"])
chain = LLMChain(llm=llm, prompt=prompt)


def get_sumamry(text: str) -> str:
    """
    Summarize the provided text using the Hugging Face LLM.
    """
    return chain.run(text)
