import requests

urls = [
    "https://www.instagram.com/p/DPZraiOkRSN/",
    "https://www.instagram.com/p/Da23OGMgfPq/",
    "https://www.instagram.com/p/DZyLQ47scKQ/",
    "https://www.instagram.com/p/DZazje7AODJ/",
    "https://www.instagram.com/p/DY0dgwdxdim/",
    "https://www.instagram.com/p/DZCkw6hlNhx/"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for url in urls:
    try:
        response = requests.get(url, headers=headers)
        print(f"{url} -> {response.status_code}")
    except Exception as e:
        print(f"{url} -> Error: {e}")
