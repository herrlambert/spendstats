import os
import pandas as pd

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'datafiles')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputfiles')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'combined_output.csv')
CATEGORY_MAP_FILE = os.path.join(os.path.dirname(__file__), 'category_mapping.csv')

def add_category_column(df):
    # Read category mapping
    mapping_df = pd.read_csv(CATEGORY_MAP_FILE)
    # Insert 'Category' after 'Date'
    if 'Date' in df.columns:
        date_idx = df.columns.get_loc('Date')
        df.insert(date_idx + 1, 'Category', '')
        df.insert(date_idx + 2, 'Subcategory', '')
        # For each mapping, assign category if match_string is in Description
        for _, row in mapping_df.iterrows():
            match_string = str(row['match_string']).strip('"').lower()
            category_value = str(row['category_value']).strip('"')
            subcategory_value = str(row.get('subcategory_value', '')).strip('"')
            mask = df['Description'].str.lower().str.contains(match_string, na=False)
            df.loc[mask, 'Category'] = category_value
            df.loc[mask, 'Subcategory'] = subcategory_value
        # Assign 'unknown' to any rows where Category is still empty
        df['Category'] = df['Category'].replace('', 'unknown')
    return df

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    all_dfs = []
    for filename in os.listdir(DATA_DIR):
        if filename.lower().endswith('.csv'):
            filepath = os.path.join(DATA_DIR, filename)
            df = pd.read_csv(filepath)
            if 'Status' in df.columns:
                df = df.drop(columns=['Status'])
            df = add_category_column(df)
            all_dfs.append(df)

    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        combined_df.to_csv(OUTPUT_FILE, index=False)
        print(f"Combined CSV written to: {OUTPUT_FILE}")
    else:
        print("No CSV files found in datafiles directory.")

if __name__ == '__main__':
    main()