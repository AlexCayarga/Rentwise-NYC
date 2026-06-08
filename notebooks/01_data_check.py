import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
data_path = project_root / "data" / "raw" / "train.json"

df = pd.read_json(data_path)

#print("Shape:", df.shape)
#print(df.columns.tolist())

print(df[["bedrooms", "price", "latitude", "longitude"]].head())

#"bathrooms", "bedrooms", "price", "latitude", "longitude", "features"