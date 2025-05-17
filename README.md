# Amazon Product Analysis

This project was completed as part of the **CITS1401: Computational Thinking with Python** course at **The University of Western Australia** (Semester 2, 2024).  
It performs multiple data analysis tasks on Amazon product and sales data using pure Python, without external modules.

## 📁 Files

- `Amazon_products.csv` – Dataset containing product metadata including category, pricing, ratings, and discount.
- `Amazon_sales.txt` – Sales data per product across years.
- `analysis.py` – Python program implementing the required tasks.

## 🧠 Tasks Overview

The program implements the following tasks via the function `main(CSVfile, TXTfile, category)`:

### 🔍 Task 1 – Identify Extreme Discount Prices
Finds the product ID with the **highest** and **lowest** discounted price for a specific category.

### 📊 Task 2 – Price Summary Statistics
Calculates:
- **Mean**
- **Median**
- **Mean Absolute Deviation (MAD)**  
...for actual prices of products in a category, **filtered by rating count > 1000**.

### 📉 Task 3 – Standard Deviation of Discount Percentages
For each category, calculates the standard deviation of discount percentages, considering only products where **3.3 ≤ rating ≤ 4.3**.

### 🔗 Task 4 – Correlation of Sales
Finds the correlation coefficient between the yearly sales of:
- The product with the highest discounted price
- The product with the lowest discounted price  
(from Task 1)

## ⚙️ How to Use

```python
from analysis import main

OP1, OP2, OP3, OP4 = main("Amazon_products.csv", "Amazon_sales.txt", "Computers&Accessories")

print(OP1)  # ['b07vtfn6hm', 'b08y5kxr6z']
print(OP2)  # [2018.8, 800, 2132.48]
print(OP3)  # [0.297, 0.2654, 0.2311, ...]
print(OP4)  # -0.0232
