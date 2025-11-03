import requests
import json
import time

all_data = []
page = 1

headers = {
    "User-Agent": "FlowerBloomApp/1.0 (your_email@example.com)"
}

while True:
    url = f"https://api.inaturalist.org/v1/observations?term_id=12&term_value_id=13&quality_grade=research&per_page=200&page={page}"
    try:
        res = requests.get(url, headers=headers).json()
    except Exception as e:
        print("Error fetching page", page, e)
        break

    if 'results' not in res:
        print("No results key in response:", res)
        break

    results = res['results']
    if not results:
        break

    all_data.extend(results)
    print(f"Page {page} -> Collected {len(results)} observations")
    page += 1
    time.sleep(1)  # polite delay to avoid being blocked

print(f"Total collected observations: {len(all_data)}")

# Extract relevant fields
flowers = []
for obs in all_data:
    if obs.get('geojson'):
        flowers.append({
            'species': obs.get('species_guess'),
            'latitude': obs['geojson']['coordinates'][1],
            'longitude': obs['geojson']['coordinates'][0],
            'date': obs.get('observed_on')
        })

# Save JSON
with open("flowers.json", "w", encoding="utf-8") as f:
    json.dump(flowers, f, indent=2, ensure_ascii=False)
