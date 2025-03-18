import pandas as pd

df = pd.read_csv("/heart_2022_no_nans.csv")

column_mapping = {}

# For each column in the dataframe, create a mapping to convert to snake_case
for col in df.columns:
    # Convert CamelCase or regular text to snake_case
    # This handles both CamelCase and regular text with spaces
    snake_case = ''.join(['_'+c.lower() if c.isupper() else c.lower() for c in col]).lstrip('_')
    # Replace spaces with underscores
    snake_case = snake_case.replace(' ', '_')
    column_mapping[col] = snake_case

# Print the mapping to verify
print("\nColumn mapping:")
for original, new in column_mapping.items():
    print(f"{original} -> {new}")

# Apply the mapping to rename the columns
df_renamed = df.rename(columns=column_mapping)

# Verify the new column names
print("\nNew column names:", df_renamed.columns.tolist())

# Save the renamed dataframe to a new file
df_renamed.to_csv("C:/Users/p9bar/Documents/python/ml-stroke-prediction/heart_2022_renamed.csv", index=False)
print("File saved with renamed headers")