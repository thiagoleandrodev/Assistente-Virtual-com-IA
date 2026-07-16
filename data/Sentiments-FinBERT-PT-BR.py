import pandas as pd

# Login using e.g. `huggingface-cli login` to access this dataset
df = pd.read_csv("hf://datasets/lucas-leme/Sentiments-FinBERT-PT-BR/sentiments.csv")
