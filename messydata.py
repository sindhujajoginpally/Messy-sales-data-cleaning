import pandas as pd  # imports the pandas library, nicknamed pd

df = pd.read_csv("messy_sales_data.csv")  # loads the CSV file into a DataFrame (a table)

print(df)  # prints the entire table
print(df.shape)  # prints (number of rows, number of columns)
print(df.columns)  # prints the list of column names
print(df.info())  # prints each column's data type and how many non-empty values it has
print(df.describe())  # prints stats (mean, min, max, etc.) for numeric columns only

print(df[df["Customer Name"].isnull()])  # prints only the row(s) where Customer Name is empty

df_cleaned = df.dropna()  # creates a separate copy with ALL rows containing any missing value removed (not actually used later)

df["Customer Name"] = df["Customer Name"].fillna("Unknown")  # fills missing Customer Name values with the text "Unknown"
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mode()[0])  # fills missing Quantity values with the most common quantity in the column

print(df.isnull().sum())  # prints how many missing values remain in each column (should all be 0 now)

print(df.duplicated().sum())  # prints how many exact duplicate rows exist
df = df.drop_duplicates()  # removes duplicate rows, keeping only the first occurrence of each

df["Customer Name"] = df["Customer Name"].str.strip()  # removes extra leading/trailing spaces from every name
df["Product"] = df["Product"].str.lower()  # converts every product name to lowercase, so casing differences don't count as different products

print(df["Customer Name"].unique())  # prints every distinct customer name, with no repeats
print(df["Product"].unique())  # prints every distinct product name, with no repeats

df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed")  # converts the Order Date column from text into real dates, handling multiple date formats
print(df["Order Date"])  # prints the cleaned, standardized dates

df["Total"] = df["Price"] * df["Quantity"]  # creates a new column: Total = Price multiplied by Quantity, for each row
print(df["Total"].sum())  # prints the overall total revenue (sum of the Total column across all rows)

city_revenue = df.groupby("City")["Total"].sum()  # groups rows by City, then sums the Total column within each city group
print(city_revenue)  # prints total revenue per city, in whatever order cities appear
print(city_revenue.sort_values(ascending=False))  # prints the same city totals, sorted from highest to lowest

ordered_most = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)  # groups by Product, sums Quantity per product, sorts highest to lowest
print(ordered_most)  # prints which products were ordered the most, by volume