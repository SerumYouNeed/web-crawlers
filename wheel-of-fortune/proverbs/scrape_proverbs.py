import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.engvid.com/english-resource/50-common-proverbs-sayings/"
OUTPUT_CSV = "proverbs.csv"

def fetch_proverbs(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")

    proverbs = []
    proverb = soup.find_all('td', class_="res_proverb_proverb")
    meaning = soup.find_all('td', class_="res_proverb_def")

    for (i, j) in zip(proverb, meaning):
        proverbs.append((i.text.strip(), j.text.strip()))

    return proverbs

def save_to_csv(data, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["proverb", "meaning"])
        writer.writerows(data)

if __name__ == "__main__":
    data = fetch_proverbs(URL)
    if data:
        save_to_csv(data, OUTPUT_CSV)
        print(f"Saved {len(data)} proverbs to {OUTPUT_CSV}")
    else:
        print("No data to save.")
