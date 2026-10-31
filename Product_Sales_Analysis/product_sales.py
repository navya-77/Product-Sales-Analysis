import pandas as pd
import matplotlib.pyplot as plt

# 1. Create the sales dataset
sales_data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"],
    "Product": ["Soap", "Soap", "Soap", "Soap",
                "Soap", "Soap", "Soap"],
    "Units_sold": [10, 15, 12, 20, 13, 50, 15]
}

# 2. Convert dictionary into DataFrame
df = pd.DataFrame(sales_data)

print("\nDAILY PRODUCT SALES")
print(df)

# 3. Basic statistical analysis
print("\n--- BASIC STATISTICS ---")

mean_sales = df["Units_sold"].mean()
median_sales = df["Units_sold"].median()
mode_sales = df["Units_sold"].mode().iloc[0]

print("Mean:", round(mean_sales, 2))
print("Median:", median_sales)
print("Mode:", mode_sales)

# 4. Variance and standard deviation
variance_sales = df["Units_sold"].var(ddof=0)
std_sales = df["Units_sold"].std(ddof=0)

print("\n--- VARIANCE AND STANDARD DEVIATION ---")
print("Population Variance:", round(variance_sales, 2))
print("Population Standard Deviation:", round(std_sales, 2))

# 5. Minimum, maximum and range
minimum_sales = df["Units_sold"].min()
maximum_sales = df["Units_sold"].max()
range_sales = maximum_sales - minimum_sales

print("\n--- SALES RANGE ---")
print("Minimum Sales:", minimum_sales)
print("Maximum Sales:", maximum_sales)
print("Range:", range_sales)

# 6. Quartiles and Interquartile Range
Q1 = df["Units_sold"].quantile(0.25)
Q2 = df["Units_sold"].quantile(0.50)
Q3 = df["Units_sold"].quantile(0.75)

IQR = Q3 - Q1

print("\n--- QUARTILES AND IQR ---")
print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("Interquartile Range:", IQR)

# 7. Outlier detection using IQR
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Units_sold"] < lower_limit) |
    (df["Units_sold"] > upper_limit)
]

print("\n--- OUTLIER DETECTION ---")
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Outliers:", outliers["Units_sold"].tolist())

# 8. Bar chart
plt.figure(figsize=(9, 5))

plt.bar(df["Day"], df["Units_sold"])

plt.title("Daily Product Sales")
plt.xlabel("Day")
plt.ylabel("Units Sold")

for i, value in enumerate(df["Units_sold"]):
    plt.text(i, value + 1, str(value), ha="center")

plt.grid(axis="y")
plt.tight_layout()
plt.show()

# 9. Line chart
plt.figure(figsize=(9, 5))

plt.plot(
    df["Day"],
    df["Units_sold"],
    marker="o"
)

plt.title("Daily Product Sales Trend")
plt.xlabel("Day")
plt.ylabel("Units Sold")

plt.grid(True)
plt.tight_layout()
plt.show()


# Interpretation of Results:-

# The analysis of daily product sales shows that Saturday recorded the highest sales of 50 units, 
# while Monday recorded the lowest sales of 10 units. The average daily sales were 19.29 units. 
# The median and mode were both 15 units, indicating that 15 was the most frequently observed sales value. 
# The IQR method identified Saturday's sales of 50 units as an outlier. 
# The bar chart compares daily sales, while the line chart displays the sales trend throughout the week.

# Project conclusion:-

# This project successfully analysed daily product sales using Python.
# Pandas was used for data manipulation and statistical calculations, while Matplotlib was used to create visualizations.
# The project helped identify sales patterns, calculate statistical measures and detect outliers. 
# This analysis can help businesses understand sales performance and make better decisions.








      
