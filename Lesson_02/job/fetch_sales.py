import os
import requests
import json
import shutil
from datetime import datetime
from dotenv import load_dotenv

# 📥 Завантаження змінних із .env
load_dotenv()

# 🔐 Токен авторизації
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
BASE_URL = "https://fake-api-vycpfa6oca-uc.a.run.app/sales"

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

def fetch_sales_data(raw_dir: str):
    print("📡 Старт запиту до API")
    print(f"🔐 AUTH_TOKEN = {AUTH_TOKEN}")

    if not AUTH_TOKEN:
        raise Exception("❌ AUTH_TOKEN не знайдено! Перевір .env")

    # 🧹 Очищаємо директорію перед записом
    if os.path.exists(raw_dir):
        shutil.rmtree(raw_dir)
    os.makedirs(raw_dir, exist_ok=True)

    page = 1
    has_more = True
    today_str = datetime.today().strftime("%Y-%m-%d")

    while has_more:
        print(f"➡️ Запит сторінки {page}...")
        response = requests.get(BASE_URL, headers=HEADERS, params={"page": page})

        if response.status_code != 200:
            raise Exception(f"❌ Помилка при запиті до API: {response.status_code}")

        data = response.json()
        items = data.get("items", [])
        has_more = data.get("has_more", False)

        filename = os.path.join(raw_dir, f"sales_{today_str}_{page}.json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)

        print(f"✅ Збережено сторінку {page} у {filename}")
        page += 1

    print("🎉 Завантаження завершено!")