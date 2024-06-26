from fastapi import FastAPI
from pydantic import BaseModel

from langchain_huggingface import HuggingFacePipeline

from llm_backend.summarizer import Summarizer


class UserText(BaseModel):
    """
    Pydantic model for user input text
    """
    input_text: str


app = FastAPI()

# Defining build in LangChain module for LLM calls.
# App uses T5Small model for summarization because it doesn't take up much disk space compared to other models.
summarizer = Summarizer(
    llm=HuggingFacePipeline.from_model_id(
            model_id="t5-small",
            task="summarization"
        )
)


# Defining endpoint
@app.post("/summarize")
def summarize(user_text: UserText) -> dict:
    """
    Summarize given user text by making LLM call
    :param user_text: Pydantic object with user input
    :return: Processed by LLM text
    """
    return {"result": summarizer.query(user_text.input_text)}

