import os
import json

def CreateUser():
    user_name = input("Enter the name of the user: ")
    user_name = user_name.title()

    if os.path.exists(rf"Users\{user_name}\Summary") and os.path.exists(rf"Users\{user_name}\storage.json"):
        print("User already exists")
    else:
        if not os.path.exists(rf"Users\{user_name}\Summary"):
            os.makedirs(rf'Users\{user_name}\Summary')
        if not os.path.exists(rf"Users\{user_name}\storage.json"):
            with open(rf"Users\{user_name}\storage.json", 'w') as f:
                json.dump({"temp": "file"}, f)
        
        print(f"User: {user_name} created")

if __name__ == "__main__":
    CreateUser()