import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain




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
    repo_id="facebook/bart-large-cnn",  
    huggingfacehub_api_token=HF_API_KEY,
    task="summarization",
    model_kwargs={"temperature": 0, "max_length": 300}
)

template = """Summarize the following article in 3-5 sentences:

{text}

Summary:"""

prompt = PromptTemplate(template=template, input_variables=["text"])
chain = LLMChain(llm=llm, prompt=prompt)


def get_summary(text: str) -> str:
    """
    Summarize the provided text using the Hugging Face LLM.
    """
    return chain.run(text)


final_sum_prompt_template = """

Summarize the following, keep contextual data, include details:

{text}

Summary:

"""

new_prompt = PromptTemplate(template=final_sum_prompt_template, input_variables=["text"])
new_chain = LLMChain(llm=llm, prompt=new_prompt)


def get_final_summ(text: str):
    return new_chain.run(text)
