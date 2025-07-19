**25 Python coding exercises** specifically designed for practicing data manipulation and analysis using the **Amazon order dataset** [amazon_order_details.csv](amazon_order_details.csv). These focus on building your **Python + Pandas** skills.

---

### 🐍 **Python Coding Exercises for Data Analysis**

#### 📦 **1. Load & Inspect Data**

1. Load the CSV file using Pandas and display the first 5 rows.
2. Print the column names and their data types.
3. Get the shape (rows, columns) of the dataset.
4. Show summary statistics for numerical columns.
5. List all unique values in the `Delivery Status` column.

#### 🧹 **2. Data Cleaning**

6. Check for missing values in each column and count them.
7. Convert the `Order Date` and `Shipping Date` columns to datetime format.
8. Remove any duplicate rows from the dataset.
9. Strip leading/trailing whitespace from all string columns.
10. Standardize column names to lowercase with underscores.

#### 🔁 **3. Data Transformation**

11. Create a new column called `delivery_days` that calculates the number of days between order and shipping.
12. Extract the `month` from the `Order Date` and add it as a new column.
13. Recalculate `total_price` using `quantity * price_per_unit` and compare with the original.
14. Add a column that marks orders with total price > \$300 as `"High Value"`, else `"Regular"`.
15. Add a column `weekday` that shows the day of the week the order was placed.

#### 📊 **4. Aggregation & Grouping**

16. Calculate the total number of orders per `City`.
17. Find the top 3 most frequently purchased items.
18. Calculate total revenue generated per `Category`.
19. Find the average delivery time per `State`.
20. Group by `Payment Method` and calculate total and average order value.

#### 📈 **5. Filtering & Sorting**

21. Filter orders where `Delivery Status` is `"Cancelled"` and `Total Price` is greater than \$100.
22. Sort the dataset by `Order Date` in descending order.
23. Display all orders where the `Quantity` is more than 3 and the `Category` is `"Electronics"`.
24. Find all orders made using `"Credit Card"` with `Total Price` above average.
25. Display the top 10 most expensive orders by `Total Price`.

---
