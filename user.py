import os

def CreateUser():
    user_name = input("Enter the name of the user: ")
    user_name = user_name.title()

    if os.path.exists(rf"Users\{user_name}"):
        print("User already exists")
    else:
        os.makedirs(rf'Users\{user_name}')
        print(f"User: {user_name} created")

if __name__ == "__main__":
    CreateUser()