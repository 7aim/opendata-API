import urllib.request
import json
import pandas as pd

# API'den veri seti bilgilerini al
url = 'https://admin.opendata.az/api/3/action/package_show?id=main-indicators-of-crime-in-azerbaijan'
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

# CSV dosyasının URL'sini al
csv_url = data["result"]["resources"][0]["url"]

# CSV dosyasını pandas ile oku
df = pd.read_csv(csv_url)

# Tabloyu ekrana yazdır
print(df)
