
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sales.csv")

# Display first five rows
print("\n===== SALES DATA =====")
print(df.head())

# Dataset information
print("\n===== DATASET INFORMATION =====")
df.info()

print("\nDataset Shape:", df.shape)

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Total revenue
print("\n===== TOTAL SALES =====")
print("Total Revenue:", df["Revenue"].sum())
print("Total Quantity Sold:", df["Quantity"].sum())

# Group by Product
product_sales = df.groupby("Product")["Revenue"].sum()

print("\n===== SALES BY PRODUCT =====")
print(product_sales)

# Group by Category
category_sales = df.groupby("Category")["Revenue"].sum()

print("\n===== SALES BY CATEGORY =====")
print(category_sales)

# Group by Region
region_sales = df.groupby("Region")["Revenue"].sum()

print("\n===== SALES BY REGION =====")
print(region_sales)

# Filter high-value sales
print("\n===== HIGH VALUE SALES =====")
print(df.loc[df["Revenue"] > 5000])

# Product chart
plt.figure(figsize=(9, 5))
product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()

# Category chart
plt.figure(figsize=(7, 5))
category_sales.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_category.png")
plt.show()

# Region chart
plt.figure(figsize=(7, 5))
region_sales.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_region.png")
plt.show()

# Save analyzed dataset
df.to_csv("analyzed_sales.csv", index=False)

print("\nAnalysis Completed Successfully!")
