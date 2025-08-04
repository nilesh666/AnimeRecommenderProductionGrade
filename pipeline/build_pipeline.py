from src.data_loader import DataLoader
from src.recommender import AnimeRecommender
from src.vector_store import VectorStore
from utils.custom_exception import CustomException
import sys
from utils.logger import logging

def main():
    try:
        logging.info("Building pipeline")

        loader = DataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")
        processed = loader.load_and_process()
        logging.info("Data processed successfully")

        vector_builder = VectorStore(processed)
        vector_builder.build_and_save_vector()
        logging.info("Vector store built successfully")

        logging.info("Pipeline built successfully")
    
    except Exception as e:
        raise CustomException(e, sys)

if __name__=="__main__":
    main()