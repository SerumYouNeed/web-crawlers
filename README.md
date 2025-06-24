# Web Crawlers

This repository contains a collection of Python-based web crawlers and data loaders used to gather and process data from public websites.

Each subfolder is dedicated to a specific project, such as collecting structured content for games, datasets, or APIs. The crawled data can be exported to CSV files or directly loaded into databases like PostgreSQL.

## Projects

- `wheel-of-fortune/` – crawlers and loaders used to collect proverbs, movie titles, and actor names for the Wheel of Fortune game.
- *More projects coming soon...*

## Structure

Each project folder typically contains:
- `crawler.py` – the spider/scraper script
- `loader.py` – a script for loading scraped data into a database
- `data/` – output folder for CSV files
- `requirements.txt` – project-specific dependencies

## Setup

1. Clone the repository
2. Navigate into a project folder
3. (Optional) Create a virtual environment
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## License

This repository is released under the MIT License.