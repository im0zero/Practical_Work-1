import requests
import json


username = "kubernetes"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()

required_data = {
    'company': user_data.get('company'),
    'created_at': user_data.get('created_at'),
    'email': user_data.get('email'),
    'id': user_data.get('id'),
    'name': user_data.get('name'),
    'url': user_data.get('url')
}

with open("result.json", "w") as f:
    json.dump(required_data, f, indent=2)