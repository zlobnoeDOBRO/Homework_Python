class Config:
    BASE_URL = "https://ru.yougile.com"
    API_URL = f"{BASE_URL}/api-v2"
    API_TOKEN = "YOUGILE_API_TOKEN"
    TEST_USER_ID = "REAL_USER_ID"

    HEADERS = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
