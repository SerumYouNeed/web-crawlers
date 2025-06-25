# Web Crawlers

This repository contains a collection of Python-based ETL pipelines used to gather, transform, and load data from public websites.

Each subfolder represents a self-contained project designed to collect structured content for games, datasets, or other applications. The crawled data can be exported to CSV files and/or loaded into databases like PostgreSQL.


## Projects

- `wheel-of-fortune/` – ETL pipeline for collecting English proverbs, movie titles, and actor names for the Wheel of Fortune game.
- *More projects coming soon...*


## Structure

Each project folder typically contains:
- `etl_pipeline.py` – a complete ETL script (scraping → transformation → loading to database)
- `logger.py` – basic logging configuration
- `etl.csv` – output/input CSV file
- `.env` – environment variables (e.g., PostgreSQL credentials)


## Setup

1. Clone the repository
2. Navigate into a project folder
3. (Optional) Create a virtual environment
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the ETL script:
   ```bash
   python etl_pipeline.py
   ```

## License

This repository is released under the MIT License.