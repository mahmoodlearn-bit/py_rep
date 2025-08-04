import pandas as pd
from sklearn.impute import SimpleImputer
excel_file = "sales data.xlsx"
df = pd.read_excel(excel_file)
print(df.head())  # Show first 5 rows
missing_value = df.isnull().sum()
print("Missing Values :")
print(missing_value[missing_value>0])

target_column = 'order_value_EUR'
imputer = SimpleImputer(strategy = 'median')
df[target_column] = imputer.fit_transform(df[[target_column]])
print("Imputer order_value_EUR Missing Values :")
print(df.isnull().sum())
target_column1 = 'device_type'
imputer = SimpleImputer(strategy = 'most_frequent')
df[target_column1] = imputer.fit_transform(df[[target_column1]]).ravel()
print("Imputer device_type Missing Values :")
print(df.isnull().sum())
# ...existing code...
print("\nVariable types in the dataset:")
print(df.dtypes)
# ...existing code...

# Find non-numeric values in 'order_value_EUR'
#non_numeric_mask = pd.to_numeric(df['order_value_EUR'], errors='coerce').isna() & df['order_value_EUR'].notna()
#non_numeric_values = df.loc[non_numeric_mask, 'order_value_EUR']
#print("\nNon-numeric values in 'order_value_EUR':")
#print(non_numeric_values)

# ...existing code...
# Example: Find non-numeric values in a column
#column_name = 'cost'  # Replace with your column name
#non_numeric_mask = pd.to_numeric(df[column_name], errors='coerce').isna() & df[column_name].notna()
#non_numeric_values = df.loc[non_numeric_mask, column_name]
#print(f"\nNon-numeric values in '{column_name}':")
#print(non_numeric_values)
#print(df.dtypes)
# ...existing code...
mixed_data = df['cost']
non_numeric_value = []
for value in mixed_data:
    if isinstance(value, str) and not value.isnumeric():
        non_numeric_value.append(value)
print("\nNon-numeric values in 'Cost':")
print(non_numeric_value)
# ...existing code...
# Example: Find non-numeric values in a column
#column_name = 'your_column_name'  # Replace with your column name
mask = (df['cost'] == 'XXX' )
df = df[~mask]
df['cost'] = df['cost'].astype(float)
print("\nData after removing non-numeric values in 'Cost':")
print(df['cost'])
# ...existing code...
df['date'] = df['date'].astype('datetime64[ns]')
print(df.dtypes)
print("\n duplicate value':")
duplicate = df[df.duplicated()]
print(duplicate)

df_no_duplicate = df.drop_duplicates()
print("\n data with oo duplicate value':")
print( df_no_duplicate)