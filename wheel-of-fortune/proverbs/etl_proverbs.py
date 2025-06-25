import pandas as pd
from logger import get_logger

logger = get_logger(__name__)

def extract(file_path):
    """
    Extract csv file from a given path.

    Args: 
        file_path (string): location of a file

    Returns:
        raw (DataFrame): pandas DataFrame
    """
    try:
        logger.info(f"Reading file: {file_path}")
        raw = pd.read_csv(file_path)
        return raw
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        raise

def transform(df):
    """
    Transfor data to keep only rows where revenue < 1500

    Args:
        df (DataFrame): data frame used in transformation

    Returns:
        df (DataFrame): transformed data where revenue is under 1500
    """
    logger.info("Filtering rows with revenue < 1500")
    df = df.loc[df["revenue"] < 1500, :]
    return df

def load(df, file_path):
    """
    Saves data to csv file under given path. Rows without indexes.

    Args:
        df (DataFrame): data given to save
        file_path (string): location of saved file

    Returns:
        file_path (string): returns path for tests
    """
    logger.info(f"Saving result to {file_path}")
    df.to_csv(file_path, index=False)

def run():
    """
    Runs every step of pipeline:
    - extraxt
    - transform
    - run
    """
    logger.info("Running simple_etl_pipeline...")
    try:
        df = extract("resources/input/sales.csv")
        df = transform(df)
        load(df, "resources/output/low_revenue.csv")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")    

if __name__ == "__main__":
    run()