import requests
import time
import csv

# Set your API Key here
API_KEY = "AIzaSyCXaIt1U23Z631tptMRlvz3d9cWOzucEVw"

# Base URL for the Google Places API
BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# Output file
output_file = "clinics_data.csv"

def fetch_clinics_data(query, api_key):
    clinics = []
    next_page_token = None
    
    while True:
        # Parameters for the request
        params = {
            "query": query,
            "key": api_key,
        }
        if next_page_token:
            params["pagetoken"] = next_page_token
        
        # Send request
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if "results" in data:
            for clinic in data["results"]:
                clinics.append({
                    "name": clinic.get("name"),
                    "address": clinic.get("formatted_address"),
                    "phone_number": clinic.get("formatted_phone_number", "N/A"),
                    "rating": clinic.get("rating", "N/A")
                })
        
        # Check if there is a next page
        next_page_token = data.get("next_page_token")
        if not next_page_token:
            break
        
        # Avoid hitting rate limits
        time.sleep(2)
    
    return clinics

def save_to_csv(clinics, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "address", "phone_number", "rating"])
        writer.writeheader()
        writer.writerows(clinics)

# Prompt the user for a query
query = input("Enter your search query (e.g., 'clinics in California'): ")

# Fetch clinics data
print("Fetching data, please wait...")
clinics_data = fetch_clinics_data(query, API_KEY)

# Save data to CSV
save_to_csv(clinics_data, output_file)

print(f"Data saved to {output_file}")
