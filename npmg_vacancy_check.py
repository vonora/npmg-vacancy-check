import difflib
import os
import time
import urllib.request
from datetime import datetime

from bs4 import BeautifulSoup

from constants import URL, DATA_FILE, DATA_FILE_MODIFIED


# =========================
# СМЕНЕНО: вече връща само text (headers + paragraphs)
# =========================
def fetch_page():
    req = urllib.request.Request(
        URL,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(req) as response:
        html = response.read().decode("utf-8", errors="ignore")

    soup = BeautifulSoup(html, "html.parser")

    items = []

    # headers
    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        text = tag.get_text(strip=True)
        if text:
            items.append("[HEADER] " + text)

    # paragraphs
    for tag in soup.find_all("p"):
        text = tag.get_text(strip=True)
        if text:
            items.append("[PARAGRAPH] " + text)

    return "\n".join(items)


def save(content, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def load(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def get_diff(old, new):
    diff = difflib.unified_diff(
        old.splitlines(),
        new.splitlines(),
        fromfile="OLD",
        tofile="NEW",
        lineterm=""
    )

    print("\n===== ПРОМЯНА ОТКРИТА =====\n")
    diff_as_str: str = ""
    for line in diff:
        if line.startswith("+") or line.startswith("-"):
            #print(line)
            diff_as_str = diff_as_str + line + "\n"

    return diff_as_str


def check():
    #print(f"[{datetime.now()}] Проверка...")

    new_page = fetch_page()
    old_page = load(DATA_FILE)

    if old_page is None:
        save(new_page, DATA_FILE)
        print("Първо запазване на страницата.")
        return None

    if new_page != old_page:
        diff_as_str = get_diff(old_page, new_page)
        save(new_page, DATA_FILE_MODIFIED)
        return diff_as_str
    else:
        print("Няма промяна.")
        return None
