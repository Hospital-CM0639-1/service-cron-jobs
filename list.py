import os

# Configuration
FOLDER_PATH = '.'

try:
    csv_files = [f for f in os.listdir(FOLDER_PATH) if f.endswith('.csv')]
    
    if csv_files:
        for file in csv_files:
            with open(file) as f:
                print(f.read())
    else:
        print("No CSV files found in the folder.")

except Exception as e:
    print(f"Error occurred: {e}")