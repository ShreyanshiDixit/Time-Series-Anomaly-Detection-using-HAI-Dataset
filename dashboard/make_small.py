import pandas as pd

# Load big dataset
df = pd.read_csv("hai-train1.csv")

# Take only first 5000 rows
df_small = df.head(5000)

# Save new file
df_small.to_csv("small.csv", index=False)

print("✅ small.csv created successfully!")