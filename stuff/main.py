"""
Requests module provides access to websites or API's so that you can get data
"""
import requests

city_name = input("What city? ").strip().lower()

# Enter your API key
API_KEY = "e45885b0a6c24285e851e98c7dfbcb1a"

# Generate the URL needed for the API call
URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

# Use request module to make an APIO call and get the data 
# Note: data will come back as a JSON object
json_data = requests.get(URL, timeout=10).json()

# Get the conditions
forecast = json_data["weather"][0]['description']

print(forecast)
