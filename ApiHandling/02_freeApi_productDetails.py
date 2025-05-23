import requests

# Correct product Id = between 1 - 100 both inclusive
def fetch_product_by_id(productId):
    api_url = f"https://api.freeapi.app/api/v1/public/randomproducts/{productId}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data["success"] and "data" in data:
            product_data = data["data"]
            title = product_data.get("title")
            brand = product_data.get("brand")
            category = product_data.get("category")
            return title, brand, category
        else:
            print("data not found in the response")
    else:
        print(f"Request failed with response code: {response.status_code}")
        return 
        

def main():
    try:
        productId = input("Enter the product Id: ")
        result = fetch_product_by_id(productId)

        if result:  # check if it's not None
            title, brand, category = result
            print(f"Product Title: {title}")
            print(f"Product Brand: {brand}")
            print(f"Product Category: {category}")
        else:
            print("Product not found.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return
    

if __name__ == "__main__":
    main()
    
