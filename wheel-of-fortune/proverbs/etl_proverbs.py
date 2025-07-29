import pandas as pd
from logger import get_logger
from bs4 import BeautifulSoup
import csv
import requests
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

URL = "https://www.engvid.com/english-resource/50-common-proverbs-sayings/"
OUTPUT_CSV = "proverbs.csv"

logger = get_logger(__name__)

def extract(url):
    """
    Extract raw data in form of a list from given url.

    Args: 
        url (string): Location of a page to scrape.

    Returns:
        proverbs (List of Dicts): List of scraped dicts in format [{proverb:proverb, meaning:meaning},]
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")

    proverbs = []
    proverb = soup.find_all('td', class_="res_proverb_proverb")
    meaning = soup.find_all('td', class_="res_proverb_def")

    for (i, j) in zip(proverb, meaning):
        proverbs.append({"proverb":i.text.strip(), "meaning":j.text.strip()})

    return proverbs

def transform(raw, file_path):
    """
    Transform data to keep nice formatting ready for save to CSV file.

    Args:
        raw (List of Dicts): Data used in transformation process.
    """
    logger.info("Punctuation checking.")
    df = pd.DataFrame(raw)
    logger.info(f"Saving result to {file_path}")
    df.to_csv(file_path, index=False)

def load(file_path):
    """
    Loads data from given path to postgres. 

    Args:
        file_path (string): Location of saved file.
    """
    logger.info(f"Loading result to to postgres from {file_path}")
    
    try:
        with psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        ) as conn:
            with conn.cursor() as cur:
                with open(file_path, newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        cur.execute("""
                                    INSERT INTO proverbs (proverb, meaning)
                                    VALUES (%s, %s)
                                    ON CONFLICT (proverb) DO NOTHING
                                    """,
                                    (row["proverb"], row["meaning"])
                        )
        logger.info("Data loaded to database successfully.")

    except Exception as e:
        logger.error(f"Database load failed: {e}")

def run():
    """
    Runs every step of pipeline:
    - extraxt
    - transform
    - run
    """
    logger.info("Running proverbs_etl_pipeline...")
    try:
        raw_data = extract(URL)
        if not raw_data:
            logger.warning("No data to transform. ETL ended.")
            return
        transform(raw_data, OUTPUT_CSV)
        load(OUTPUT_CSV)
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")    

if __name__ == "__main__":
    run()