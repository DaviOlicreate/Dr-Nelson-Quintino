import urllib.request
import re
import os

urls = [
    ("https://www.instagram.com/p/DPZraiOkRSN/", "ig_1.jpg"),
    ("https://www.instagram.com/p/Da23OGMgfPq/", "ig_2.jpg"),
    ("https://www.instagram.com/p/DZyLQ47scKQ/", "ig_3.jpg"),
    ("https://www.instagram.com/p/DZazje7AODJ/", "ig_4.jpg"),
    ("https://www.instagram.com/p/DY0dgwdxdim/", "ig_5.jpg"),
    ("https://www.instagram.com/p/DZCkw6hlNhx/", "ig_6.jpg"),
]

os.makedirs("assets/images/instagram", exist_ok=True)

for url, filename in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # Find og:image
        match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
        if match:
            img_url = match.group(1).replace("&amp;", "&")
            print(f"Downloading {filename} from {img_url[:50]}...")
            urllib.request.urlretrieve(img_url, f"assets/images/instagram/{filename}")
        else:
            print(f"No og:image found for {url}")
    except Exception as e:
        print(f"Error on {url}: {e}")
