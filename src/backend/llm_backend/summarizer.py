from langchain_core.language_models import BaseLLM


class Summarizer:
    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def query(self, text: str) -> str:
        """
        Make LLM call to summarize given text
        :param text: Given text
        :return: Processed text
        """
        return self.llm.invoke(text)
