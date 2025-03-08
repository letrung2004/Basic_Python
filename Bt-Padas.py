import pandas as pd

# 1
# Read the TSV file
df = pd.read_csv("05_gap-merged-with-china-1952.tsv", sep="\t")

# Display the first 5 lines
print(df.head())

# 2
num_rows, num_columns = df.shape

print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")


# 3. Print the column names
print("Column names:", df.columns)

# 4. Print the type of column names
print("Type of column names:", type(df.columns))

# 5. Get the 'country' column and store it in a variable
country_column = df["country"]
print("First 5 observations of 'country':\n", country_column.head())

# 6. Show the last 5 observations of the 'country' column
print("Last 5 observations of 'country':\n", country_column.tail())

# 7. Show the first and last 5 observations of 'country', 'continent', and 'year' columns
subset_columns = df[['country', 'continent', 'year']]
print("First 5 observations:\n", subset_columns.head())
print("Last 5 observations:\n", subset_columns.tail())


# 8. Get the first row and the 100th row
first_row = df.iloc[0]
hundredth_row = df.iloc[99]  # Since indexing starts from 0

print("First row:\n", first_row)
print("100th row:\n", hundredth_row)

# 9. Get the first column using an integer index
first_column = df.iloc[:, 0]  # First column
print("First column:\n", first_column.head())

# Get the first and last column using integer index
first_and_last_column = df.iloc[:, [0, -1]]  # First and last columns
print("First and Last column:\n", first_and_last_column.head())

# 10. Get the last row using .loc
try:
    last_row_loc = df.loc[-1]  # This will raise an error because .loc does not support negative indices
except KeyError:
    print("Using .loc[-1] does not work!")

# Correct way to get the last row
last_row = df.iloc[-1]  # iloc allows negative indexing
print("Last row:\n", last_row)

# 11. Select the first, 100th, and 1000th rows using two methods
selected_rows1 = df.iloc[[0, 99, 999]]  # Method 1 using iloc
selected_rows2 = df.loc[df.index[[0, 99, 999]]]  # Method 2 using loc

print("Selected rows (Method 1):\n", selected_rows1)
print("Selected rows (Method 2):\n", selected_rows2)

# 12. Get the 43rd country using .loc and .iloc
country_43_loc = df.loc[42, "country"]  # Assuming the country column is named "country"
country_43_iloc = df.iloc[42, df.columns.get_loc("country")]

print("43rd country using .loc:", country_43_loc)
print("43rd country using .iloc:", country_43_iloc)

# 13. Get the first, 100th, and 1000th rows from the first, 4th, and 6th columns
selected_data = df.iloc[[0, 99, 999], [0, 3, 5]]
print("Selected data:\n", selected_data)

# 14. Get the first 10 rows
first_10_rows = df.head(10)
print("First 10 rows:\n", first_10_rows)

# 15. Average life expectancy per year
# average_life_expectancy = df.groupby("year")["life_expectancy"].mean()
# print("Average life expectancy per year:\n", average_life_expectancy)

# 16. Subsetting method for 15 (selecting only the required columns first)
# subset = df[["year", "life_expectancy"]]
# average_life_expectancy_subset = subset.groupby("year")["life_expectancy"].mean()
# print("Average life expectancy per year (subsetting method):\n", average_life_expectancy_subset)
#
# # 17. Create a Series with index 0 for ‘banana’ and index 1 for ‘42’
# series1 = pd.Series(["banana", 42], index=[0, 1])
# print("Series with custom index:\n", series1)
#
# # 18. Similar to 17, but change index names
# series2 = pd.Series(["Wes McKinney", "Creator of Pandas"], index=["Person", "Who"])
# print("Series with custom string index:\n", series2)
#
# # 19. Create a dictionary with Pandas DataFrame
# data = {
#     "Occupation": ["Chemist", "Statistician"],
#     "Born": ["1920-07-25", "1876-06-13"],
#     "Died": ["1958-04-16", "1937-10-16"],
#     "Age": [37, 61]
# }
# df_dict = pd.DataFrame(data, index=["Franklin", "Gosset"])
# print("DataFrame from dictionary:\n", df_dict)