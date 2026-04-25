import os
import time

import requests
from dotenv import load_dotenv

# Загружаем .env
load_dotenv()
PANEL_URL = os.getenv("MARZBAN_URL", "https://PANEL.DOMAIN")
ADMIN_USER = os.getenv("MARZBAN_USER", "admin")
ADMIN_PASS = os.getenv("MARZBAN_PASS", "password")

KIDS_INBOUND_TAG = os.getenv("KIDS_INBOUND_TAG", "VLESS_KIDS")


def get_admin_token() -> str:
    # Marzban: POST /api/admin/token (x-www-form-urlencoded, grant_type=password) :contentReference[oaicite:5]{index=5}
    url = f"{PANEL_URL}/api/admin/token"
    data = {
        "grant_type": "password",
        "username": ADMIN_USER,
        "password": ADMIN_PASS,
    }
    r = requests.post(url, data=data, timeout=15, verify=False)
    r.raise_for_status()
    js = r.json()
    return js["access_token"]


def create_kids_user(token: str, username: str, days: int = 30, data_limit_gb: int = 0):
    # Marzban: POST /api/user :contentReference[oaicite:6]{index=6}
    url = f"{PANEL_URL}/api/user"
    headers = {"Authorization": f"Bearer {token}"}

    expire_ts = int(time.time()) + days * 24 * 3600
    data_limit_bytes = 0 if data_limit_gb <= 0 else data_limit_gb * 1024**3

    payload = {
        "username": username,
        "expire": expire_ts,
        "data_limit": data_limit_bytes,
        "status": "active",
        # Важно: привязываем ТОЛЬКО к inbound'у kids
        "inbounds": {"vless": [KIDS_INBOUND_TAG]},
        # proxies можно оставить пустым или задать параметры протокола.
        # Если у тебя в панели уже "шаблон/дефолт", часто достаточно не усложнять.
        "proxies": {"vless": {}},
    }

    r = requests.post(url, json=payload, headers=headers, timeout=15)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    token = get_admin_token()
    print(token)
    user = create_kids_user(token, username="kids_user_001", days=30, data_limit_gb=0)
    print("Created user:", user.get("username"))
