import json
import math
from typing import List, Dict, Any

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great circle distance between two points on Earth in kilometers.
    """
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of Earth in kilometers
    r = 6371
    return c * r

def remove_nearby_coordinates(data: List[Dict[str, Any]], distance_threshold: float = 0.1) -> List[Dict[str, Any]]:
    """
    Remove entries that have coordinates very close to each other.
    
    Args:
        data: List of dictionaries containing flower data
        distance_threshold: Distance in kilometers below which coordinates are considered "nearby"
    
    Returns:
        Filtered list with nearby coordinates removed
    """
    filtered_data = []
    
    for i, current_item in enumerate(data):
        is_nearby = False
        
        # Check if current item is near any item already in filtered_data
        for existing_item in filtered_data:
            distance = haversine_distance(
                current_item['latitude'], current_item['longitude'],
                existing_item['latitude'], existing_item['longitude']
            )
            
            if distance < distance_threshold:
                is_nearby = True
                break
        
        # If not nearby any existing item, add it to filtered_data
        if not is_nearby:
            filtered_data.append(current_item)
    
    return filtered_data

def remove_date_field(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Remove the 'date' field from each dictionary in the data.
    
    Args:
        data: List of dictionaries containing flower data
    
    Returns:
        List of dictionaries with 'date' field removed
    """
    return [{k: v for k, v in item.items() if k != 'date'} for item in data]

def process_flowers_data(input_file: str, output_file: str, distance_threshold: float = 0.1):
    """
    Process the flowers JSON data by removing dates and nearby coordinates.
    
    Args:
        input_file: Path to input JSON file
        output_file: Path to output JSON file
        distance_threshold: Distance threshold in kilometers for considering coordinates as "nearby"
    """
    print(f"Loading data from {input_file}...")
    
    # Load the JSON data
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Loaded {len(data)} flower entries")
    
    # Remove date fields
    print("Removing date fields...")
    data_no_dates = remove_date_field(data)
    
    # Remove nearby coordinates
    print(f"Removing nearby coordinates (threshold: {distance_threshold} km)...")
    filtered_data = remove_nearby_coordinates(data_no_dates, distance_threshold)
    
    print(f"After filtering: {len(filtered_data)} entries remaining")
    print(f"Removed {len(data) - len(filtered_data)} entries")
    
    # Save the processed data
    print(f"Saving processed data to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, indent=2, ensure_ascii=False)
    
    print("Processing complete!")

if __name__ == "__main__":
    # Configuration
    input_file = "flowers.json"
    output_file = "flowers_processed.json"
    distance_threshold = 10  # kilometers - adjust this value as needed
    
    # You can adjust the distance_threshold based on your needs:
    # - 0.01 km (10 meters) for very close points
    # - 0.1 km (100 meters) for reasonably close points  
    # - 1.0 km for points that are somewhat close
    
    process_flowers_data(input_file, output_file, distance_threshold)
