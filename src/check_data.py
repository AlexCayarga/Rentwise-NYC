import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
data_path = project_root / "data" / "raw" / "train.json"

df = pd.read_json(data_path)

#print("Shape:", df.shape)
#print(df.columns.tolist())
#duplicate_ids = df["listing_id"].duplicated()
#print("Number of duplicate listing IDs:", duplicate_ids.sum())
#print(df[["features"]].tail().to_string())
#print(df.dtypes)
#print(df.isnull().sum())
#print(df["bathrooms"].value_counts().sort_index())
#print(df["price"].describe())
#"bathrooms", "bedrooms", "price", "latitude", "longitude", "features"