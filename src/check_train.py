import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
data_path = project_root / "data" / "processed" / "column_cleaned_train.csv"

df = pd.read_csv(data_path)

#print("Shape:", df.shape)
#print(df.columns.tolist())
duplicates = df["listing_id"].duplicated()
print(duplicates.sum())
#print(df[["features"]].tail().to_string())
#print(df.dtypes)
#print(df.isnull().sum())
#print(df["bathrooms"].value_counts().sort_index())
#print(df["price"].describe())
#"bathrooms", "bedrooms", "price", "latitude", "longitude", "features"