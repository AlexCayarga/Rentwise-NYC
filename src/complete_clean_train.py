import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
data_path = project_root / "data" / "processed" / "column_cleaned_train.csv"

df = pd.read_csv(data_path)




# Save cleaned data
#output_path = project_root / "data" / "processed" / "completely_cleaned_train.csv"
#df.to_csv(output_path, index=False)

#print("Saved cleaned data to:", output_path)
print(df.head())
print(df.columns)