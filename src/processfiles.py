import os
import pandas as pd

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'datafiles')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputfiles')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'combined_output.csv')

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
            all_dfs.append(df)

    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        combined_df.to_csv(OUTPUT_FILE, index=False)
        print(f"Combined CSV written to: {OUTPUT_FILE}")
    else:
        print("No CSV files found in datafiles directory.")

if __name__ == '__main__':
    main()