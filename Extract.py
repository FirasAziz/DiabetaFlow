import requests
import json
import os

# Function to fetch data and append it to the existing file
def fetch_and_save_data():
    url = "http://87.236.232.200:5000/data"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        
        # Save the combined data back to the file
        with open("/home/hadoop/DE2/diabetes.json", "w") as f:
                json.dump(data, f)   

        print(f"Data extraction completed! {len(data)} new records added. Total records: {len(data)}.")
    else:
        print(f"Failed to fetch data: Status Code {response.status_code}")



