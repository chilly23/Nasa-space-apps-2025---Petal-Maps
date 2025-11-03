import json
import math

def distance_between_points(lat1, lon1, lat2, lon2):
    """Calculate distance between two points in kilometers"""
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return 6371 * c  # Earth's radius in km

# Load the data
with open('flowers.json', 'r', encoding='utf-8') as f:
    flowers = json.load(f)

print(f"Original data: {len(flowers)} entries")

# Remove date field and filter nearby coordinates
processed_flowers = []
distance_threshold = 200  # km - change this value as needed

for flower in flowers:
    # Remove date field
    flower_clean = {k: v for k, v in flower.items() if k != 'date'}
    
    # Check if this flower is near any already processed flower
    is_nearby = False
    for existing in processed_flowers:
        distance = distance_between_points(
            flower_clean['latitude'], flower_clean['longitude'],
            existing['latitude'], existing['longitude']
        )
        if distance < distance_threshold:
            is_nearby = True
            break
    
    # If not nearby, add it to processed list
    if not is_nearby:
        processed_flowers.append(flower_clean)

print(f"After processing: {len(processed_flowers)} entries")
print(f"Removed {len(flowers) - len(processed_flowers)} nearby entries")

# Save the processed data
with open('flowers_processed.json', 'w') as f:
    json.dump(processed_flowers, f, indent=2)

print("Done! Check 'flowers_processed.json' for the result.")
