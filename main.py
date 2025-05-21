import urllib.request
import json
import pandas as pd

url = 'https://admin.opendata.az/api/3/action/package_show?id=main-indicators-of-crime-in-azerbaijan'
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

csv_url = data["result"]["resources"][0]["url"]

df = pd.read_csv(csv_url)

print(df)
