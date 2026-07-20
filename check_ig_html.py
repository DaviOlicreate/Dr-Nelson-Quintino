import urllib.request
try:
    url = "https://www.instagram.com/p/DPZraiOkRSN/embed"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    if "O link desta foto" in html or "Broken" in html:
        print("Instagram returns BROKEN LINK page for the embed.")
    else:
        print("Instagram returns normal embed.")
except Exception as e:
    print(e)
