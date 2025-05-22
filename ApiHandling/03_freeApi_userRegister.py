import requests

def user_registration(username, role, password, email):
    api_url = "https://api.freeapi.app/api/v1/users/register"
    
    payload = {
        "username": username,
        "role": role,
        "password": password,
        "email": email
    }
    
    # The following is not required as we are using "import requests"
    # headers = {
    # "Content-Type": "application/json"
    # }
    
    response = requests.post(api_url, json=payload)
    
    if(response.status_code) == 201:
        print("User registered Successfully")
    else:
        print(f"Registration failed. {response.status_code}")
        print(response.json())


def main():
    usr_name = input("Enter the user name: ")
    usr_email = input("Enter the email id: ")
    usr_pass = input("Enter password: ")
    usr_role = input("Enter the user role: ")
    
    user_registration(usr_name, usr_role, usr_pass, usr_email)


if __name__ == "__main__":
    main()