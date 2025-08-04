from src.data_loader import DataLoader
from src.recommender import AnimeRecommender
from src.vector_store import VectorStore
from utils.logger import logging
from utils.custom_exception import CustomException
import sys
from config.config import GROQ_API_KEY, MODEL_NAME

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir = "chroma_db"):
        try:

            logging.info("Initializing recommendation pipeline")

            vector_builder = VectorStore(csv_path="", persist_directory=persist_dir)
            
            retriever = vector_builder.load_vector_store().as_retriever()
            
            self.recommender = AnimeRecommender(
                retriever, 
                GROQ_API_KEY,
                MODEL_NAME
            )
            
            logging.info("Pipeline Initialized")


        except Exception as e:
            raise CustomException(e, sys)
        
    def recommend(self, query:str, output:str):
        try:
            
            logging.info(f"Recieved the query from the user and the query is {query}")
            
            recommend = self.recommender.get_recommendation(query)
            
            logging.info("Recommendation generated successfully")
            
            return recommend
        
        except Exception as e:
            
            raise CustomException(e, sys)