from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.propmpt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retreiver, api_key:str, model_name:str):
        self.llm = ChatGroq(api_key=api_key, model_name=model_name, tempreature=0)
        self.prompt = get_anime_prompt()
        self.qa_chain = RetrievalQA.from_chain_type(
            llm = self.llm,
            chain_type = 'stuff',
            retreiver = retreiver,
            return_source_documents = True,
            chain_type_kwargs={"prompt": self.prompt}
        )

    def get_recommendation(self, query):
        result = self.qa_chain({"query":query})
        return result['result']




