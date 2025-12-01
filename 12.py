import tkinter as tk
import requests
import json


def get_user():
    username = entry.get()
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


root = tk.Tk()
root.title("GitHub user")

root.geometry("400x200")   
entry = tk.Entry(root, width=40)  
entry.pack(pady=10)

btn = tk.Button(root, text="OK", command=get_user)
btn.pack(pady=10)

root.mainloop()
