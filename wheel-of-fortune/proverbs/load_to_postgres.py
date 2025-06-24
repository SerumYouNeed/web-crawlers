import csv
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

CSV_FILE = "proverbs.csv"

def load_csv_to_db(csv_file):
    conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
    
    cur = conn.cursor()

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO proverbs (proverb, meaning) VALUES (%s, %s)",
                (row["proverb"], row["meaning"])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("Data has been loaded to db.")

if __name__ == "__main__":
    load_csv_to_db(CSV_FILE)