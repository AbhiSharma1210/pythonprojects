import requests

def fetch_user_details():
    api_url = "https://api.freeapi.app/api/v1/public/randomusers"
    response = requests.get(api_url)
    # print(response)
    if response.status_code == 200:
        # print(response.status_code)
        data = response.json()
    
        if data["success"] and "data" in data:
            user_data = data["data"]["data"]
            
            for user in user_data:
                country = user.get("location", {}).get("country")
                street = user.get("location", {}).get("street").get("name")
                print(f"Country: {country}, Street: {street}")
            
        else:
            print("Data not found in the response")
    
    else:
        print(f"Request failed with response code: {response.status_code}")
        
    

fetch_user_details()