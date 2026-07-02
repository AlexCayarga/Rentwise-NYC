import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
data_path = project_root / "data" / "processed" / "column_cleaned_train.csv"

df = pd.read_csv(data_path)

df["price_per_bedroom"] = df["price"] / df["bedrooms"].clip(lower=1)

df = df[
    ((df['latitude'] >= 40.4900) & (df['latitude'] <= 40.9166)) &
    ((df['longitude'] >= -74.2600) & (df['longitude'] <= -73.7000)) &
    ((df['bathrooms'] <= 4) & (df['bathrooms'] >= 1)) &
    (df["price"] >= 1000) &
    (df["price"] <= 10000) &
    (df["bedrooms"] <= 5) &
    (
        ((df['bedrooms'] > 1) & (df["price_per_bedroom"] <= 2500)) | 
        ((df['bedrooms'] <= 1) & (df["price"] <= 5000))
    )
].copy()

df["num_features"] = df["num_features"].clip(upper=20)        
df = df.drop(columns= "price_per_bedroom")
df = df.drop_duplicates(subset=["listing_id"])

# Save cleaned data
output_path = project_root / "data" / "processed" / "completely_cleaned_train.csv"
df.to_csv(output_path, index=False)

#print("Saved cleaned data to:", output_path)
print(df.shape)