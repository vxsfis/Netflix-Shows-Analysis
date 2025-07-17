import pandas as pd

input_file = r'C:\Users\jacks\Onedrive\Desktop\Projects\Netflix shows\netflix_titles.csv'
output_file = r'C:\Users\jacks\Onedrive\Desktop\Projects\Netflix shows\netflix_genres_exploded_cleaned.csv'

df = pd.read_csv(input_file)

# Explode genres
df['genre'] = df['listed_in'].str.split(', ')
df_exploded = df.explode('genre')

# Remove blank genres
df_exploded = df_exploded[df_exploded['genre'].notna() & (df_exploded['genre'].str.strip() != '')]

# Format 'date_added' to MM/DD/YYYY
if 'date_added' in df_exploded.columns:
    df_exploded['date_added'] = pd.to_datetime(df_exploded['date_added'], errors='coerce').dt.strftime('%m/%d/%Y')

# Remove any row with any blank in any column
df_exploded = df_exploded.dropna(how='any')

df_exploded.to_csv(output_file, index=False)

print(f'Saved cleaned file with formatted dates and no blanks to {output_file}')
