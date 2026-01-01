#!/usr/bin/env python3

import os
import re
import time
from urllib.parse import quote, urlparse

import requests
from bs4 import BeautifulSoup

# --- НАСТРОЙКИ ---
IMAGES_PER_QUERY = 4
OUTPUT_FOLDER = "source/img"

queries = [
    "inventors brainstorming png funny sketch people thinking",
    "idea lightbulb png floating above scientists heads",
    "engineer drawing prototypes png whiteboard style",
    "group of inventors png retro tech brainstorm",
    "victorian engineers png cartoon problem solving",
]


# --- ПОИСК ИЗОБРАЖЕНИЙ БЕЗ API (Google Images) ---
def get_image_urls(query):
    print(f"Ищу картинки по запросу: {query}")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    url = f"https://www.google.com/search?q={quote(query)}&tbm=isch"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        image_urls = []

        # Ищем изображения в img тегах
        for img in soup.find_all("img"):
            src = img.get("src") or img.get("data-src")
            if src and src.startswith("http") and "gstatic" not in src:
                image_urls.append(src)
                if len(image_urls) >= IMAGES_PER_QUERY:
                    break

        # Если не нашли, ищем в скриптах
        if len(image_urls) < IMAGES_PER_QUERY:
            for script in soup.find_all("script"):
                if script.string:
                    urls = re.findall(
                        r'https?://[^\s",]+\.(?:jpg|jpeg|png|gif|webp)', script.string
                    )
                    for u in urls:
                        if u not in image_urls and "gstatic" not in u:
                            image_urls.append(u)
                            if len(image_urls) >= IMAGES_PER_QUERY:
                                break
                if len(image_urls) >= IMAGES_PER_QUERY:
                    break

        print(f"✔ Найдено {len(image_urls)} изображений")
        return image_urls[:IMAGES_PER_QUERY]

    except Exception as e:
        print(f"❌ Ошибка поиска: {e}")
        return []


# --- СКАЧИВАНИЕ ФАЙЛОВ ---
def download_image(url, folder, query_index, img_index):
    try:
        print(f"⬇ Скачиваю {url[:60]}...")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

        data = requests.get(url, timeout=10, headers=headers).content

        # Определяем расширение
        ext = ".jpg"
        if ".png" in url.lower():
            ext = ".png"
        elif ".gif" in url.lower():
            ext = ".gif"
        elif ".webp" in url.lower():
            ext = ".webp"

        filename = os.path.join(folder, f"query_{query_index}_img_{img_index}{ext}")

        with open(filename, "wb") as f:
            f.write(data)

        print(f"✔ Сохранено: {filename}")
        return True

    except Exception as e:
        print(f"❌ Ошибка скачивания {url[:60]} — {e}")
        return False


# --- MAIN ---
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
print(f"📁 Папка для сохранения: {OUTPUT_FOLDER}\n")

total_downloaded = 0

for idx, q in enumerate(queries, start=1):
    print(f"\n{'=' * 60}")
    print(f"[{idx}/{len(queries)}] Запрос: {q}")
    print(f"{'=' * 60}")

    urls = get_image_urls(q)

    if not urls:
        print("⚠ Не найдено изображений для этого запроса")
        continue

    for i, u in enumerate(urls, start=1):
        if download_image(u, OUTPUT_FOLDER, idx, i):
            total_downloaded += 1
        time.sleep(0.5)  # Задержка между запросами

    time.sleep(1)  # Задержка между запросами

print(f"\n{'=' * 60}")
print(f"🎉 Готово! Загружено {total_downloaded} изображений в {OUTPUT_FOLDER}")
print(f"{'=' * 60}")
