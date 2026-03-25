# Assignment: Data Doctor

import pandas as pd

# -----------------------------
# Create Sample Dataset
# -----------------------------
data = {
    "Name": ["Zoro", "Luffy", "Nami", "Robin", "Sanji", "Zenitsu", "Luffy"],
    "City": ["Tokyo", "TOKYO", "osaka", "Kyoto", "OSAKA", "tokyo", "TOKYO"],
    "Marks": [85, 90, None, 92, 88, None, 90]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# -----------------------------
# Handle Missing Values
# -----------------------------
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# -----------------------------
# Remove Duplicate Rows
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Standardize Text (make same format)
# -----------------------------
df["City"] = df["City"].str.lower()

# -----------------------------
# Cleaned Dataset
# -----------------------------
print("\nCleaned Dataset:\n")
print(df)

# -----------------------------
# Why Data Cleaning Matters
# -----------------------------
print("\nWhy Data Cleaning Matters:")
print("1. Cleaning removes missing or incorrect data.")
print("2. It improves accuracy of analysis.")
print("3. Removing duplicates prevents wrong calculations.")
print("4. Standardizing text keeps data consistent.")
print("5. Clean data helps in better decision making.")