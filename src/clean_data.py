import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
data_path = project_root / "data" / "raw" / "train.json"

df = pd.read_json(data_path)

# Keep only useful columns
df_clean = df[[
    "bedrooms",
    "bathrooms",
    "latitude",
    "listing_id",
    "longitude",
    "price",
    "features"
]].copy()

# Join features to search
df_clean["features_text"] = df_clean["features"].apply(lambda x: " ".join(x).lower())

# Create useful amenity columns
df_clean["has_laundry"] = df_clean["features_text"].str.contains("laundry").astype(int)
df_clean["has_elevator"] = df_clean["features_text"].str.contains("elevator").astype(int)
df_clean["has_doorman"] = df_clean["features_text"].str.contains("doorman").astype(int)
df_clean["has_dishwasher"] = df_clean["features_text"].str.contains("dishwasher").astype(int)
df_clean["has_hardwood"] = df_clean["features_text"].str.contains("hardwood").astype(int)
df_clean["has_no_fee"] = df_clean["features_text"].str.contains("no fee").astype(int)
df_clean["pets_allowed"] = df_clean["features_text"].str.contains("cats allowed|dogs allowed").astype(int)

# Count number of listed features
df_clean["num_features"] = df_clean["features"].apply(len)

# Studio column
df_clean["is_studio"] = (df_clean["bedrooms"] == 0).astype(int)

# Drop the original list/text columns
df_clean = df_clean.drop(columns=["features", "features_text"])

# Save cleaned data
output_path = project_root / "data" / "processed" / "cleaned_rentals.csv"
df_clean.to_csv(output_path, index=False)

print("Saved cleaned data to:", output_path)
print(df_clean.head())
print(df_clean.columns)