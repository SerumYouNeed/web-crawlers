# Wheel of Fortune – Proverbs Crawler

This module collects English proverbs from external websites and prepares them for use in the **Wheel of Fortune** game project.

## Structure

- `scrape_proverbs.py` – Scrapes proverbs and their meanings from a website and saves them into a CSV file.
- `load_proverbs_to_db.py` – Loads the CSV data into a PostgreSQL database with a table structure:

```sql
CREATE TABLE proverbs (
    id SERIAL PRIMARY KEY,
    proverb TEXT NOT NULL,
    meaning TEXT NOT NULL
);
```

## Usage

1. Run the scraper to collect data:

```bash
python scrape_proverbs.py
```

2. Run the loader to insert into the database:

```bash
python load_proverbs_to_db.py
```

## Dependencies

This module uses:
- requests
- beautifulsoup4
- pandas
- psycopg2-binary

All dependencies are listed in the main requirements.txt.