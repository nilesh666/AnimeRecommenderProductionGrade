import pandas as pd

class DataLoader:
    def __init__(self, original_csv:str, processed_csv:str):
        self.original = original_csv
        self.processed = processed_csv
    
    def load_and_process(self):
        df = pd.read_csv(self.original, encoding='utf-8', error_bad_lines=False).dropna()
        required_cols = {'Name', 'Genres', 'sypnopsis'}   
        missing = required_cols - set(df.columns)

        if missing:
            raise ValueError("Missing columns in raw data")     
        
        df['combined_info'] = (
            "Title: "+ df["Name"] + " Overview: "+ df["sypnopsis"]+ " Genres: "+df["Genres"]
        )

        df[["combined_info"]].to_csv(self.processed, index=False, encoding='utf-8')

        return self.processed