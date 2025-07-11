import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams['font.family'] = 'DejaVu Sans'
mpl.rcParams['axes.unicode_minus'] = False

import pandas as pd
import seaborn as sns
import re
import numpy as np

df = pd.read_csv("hotel_simplified.csv")

def extract_score(text):
    match = re.search(r'(\d\.\d+)', str(text))
    return float(match.group(1)) if match else np.nan

def extract_discount(text):
    match = re.search(r'(\d+)%', str(text))
    return int(match.group(1)) if match else 0

def extract_price(text):
    match = re.search(r'(\d{1,3}(,\d{3})*)円', str(text))
    if match:
        price_str = match.group(1).replace(',', '')
        return int(price_str)
    return np.nan


df["Score"] = df["Like12"].apply(extract_score)
df["Discount (%)"] = df["justifycenter"].apply(extract_discount)
df["Price (Yen)"] = df["textgray80016"].apply(extract_price)
df = df.rename(columns={"タイトル": "Hotel Name"})
hotel_names = df["Hotel Name"]

plt.figure(figsize=(12, 6))
sns.barplot(x=df["Score"], y=hotel_names, palette="coolwarm")
plt.title("Score by Hotel")
plt.xlabel("Score")
plt.ylabel("Hotel Name")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x=df["Discount (%)"], y=hotel_names, palette="YlGnBu")
plt.title("Discount Rate (%) by Hotel")
plt.xlabel("Discount Rate (%)")
plt.ylabel("Hotel Name")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x=df["Price (Yen)"], y=hotel_names, palette="OrRd")
plt.title("Minimum Price (Yen) by Hotel")
plt.xlabel("Price (Yen)")
plt.ylabel("Hotel Name")
plt.tight_layout()
plt.show()
