import pandas as pd
import os
from datetime import datetime

def ingest_data():
    try:
        # File path
        file_path = os.path.join("data", "raw", "retail.csv")

        # Read dataset
        df = pd.read_csv(file_path)

        print("✅ Dataset Loaded Successfully!\n")

        # Create processed folder
        os.makedirs("data/processed", exist_ok=True)

        # Save cleaned file
        df.to_csv("data/processed/sales_cleaned.csv", index=False)

        # Create daily ingest folder with today's date
        today = datetime.today().strftime("%Y-%m-%d")
        daily_path = f"data/daily_ingest/{today}"
        os.makedirs(daily_path, exist_ok=True)

        df.to_csv(f"{daily_path}/sales_cleaned.csv", index=False)

        print("✅ Files saved successfully!")

    except Exception as e:
        print("❌ Error occurred:")
        print(e)


if __name__ == "__main__":
    ingest_data()