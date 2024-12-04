#%%
import pandas as pd

# %%
# Relative path to the CSV file
file_path = "./csv/drug_data.csv"

# Load the CSV file
albumin_df = pd.read_csv(file_path, sep=",", index_col=None)

# %%
# Filter the DataFrame for active ingredients containing specific keywords
keywords = ["albumin", "immunoglobulin", "coagulation"]
filtered_df = albumin_df[albumin_df["Active Ingredients"].str.contains('|'.join(keywords), case=False, na=False)]

# %%
print(filtered_df)

# %%
filtered_df.to_csv("Registered Albumin.csv", index=False,)
# %%
