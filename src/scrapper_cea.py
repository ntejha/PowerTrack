import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://npp.gov.in/publishedReports"

os.makedirs("Daily", exist_ok=True)
os.makedirs("Monthly", exist_ok=True)

def sanitize_filename(name):
    """Remove invalid characters and format nicely."""
    return re.sub(r'[^A-Za-z0-9]+', '_', name.strip()).strip('_')

def download_excel(url, folder, filename):
    """Download the Excel file and save it."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_path = os.path.join(folder, filename)
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"✅ Saved: {file_path}")
    else:
        print(f"❌ Failed to download: {url}")

def scrape_site():
    resp = requests.get(BASE_URL)
    soup = BeautifulSoup(resp.text, "html.parser")

    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.endswith(".xls") or href.endswith(".xlsx"):
            full_url = urljoin(BASE_URL, href)

            if "daily" in href.lower():
                folder = "Daily"
            elif "monthly" in href.lower():
                folder = "Monthly"
            else:
                continue

            li_tag = link.find_parent("li")
            p_tag = li_tag.find("p", class_="mp01") if li_tag else None
            title_text = p_tag.get_text(strip=True) if p_tag else "Report"

            match = re.match(r"(\d{2})\s*(.*)", title_text)
            if match:
                index_number = match.group(1)
                title = sanitize_filename(match.group(2))
            else:
                index_number = "00"
                title = sanitize_filename(title_text)

            filename = f"{index_number}_{title}.xlsx"
            download_excel(full_url, folder, filename)

if __name__ == "__main__":
    scrape_site()
