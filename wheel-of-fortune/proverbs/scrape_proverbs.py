import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.engvid.com/english-resource/50-common-proverbs-sayings/"
OUTPUT_CSV = "proverbs.csv"

def fetch_proverbs(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    proverbs = []
    # for strong_tag in soup.select("div.post-content strong"):
    #     text = strong_tag.get_text(strip=True)
    #     if "-" in text:  # np: "A picture is worth a thousand words – Better to show than to tell."
    #         proverb, meaning = map(str.strip, text.split("-", 1))
    #         proverbs.append((proverb, meaning))
    # return proverbs
    proverb = soup.find_all('td', class_="res_proverb_proverb")
    meaning = soup.find_all('td', class_="res_proverb_def")
    for i in zip(proverb, meaning):
        

    # print(proverb)
    # return proverbs

def save_to_csv(data, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["proverb", "meaning"])
        writer.writerows(data)

if __name__ == "__main__":
    fetch_proverbs(URL)
    # data = fetch_proverbs(URL)
    # save_to_csv(data, OUTPUT_CSV)
    # print(f"Saved {len(data)} proverbs to {OUTPUT_CSV}")