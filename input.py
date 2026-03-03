from datetime import datetime 
import json
import time
import user 
import os

class task:
    def __init__(self,time_submitted,category='misc',sub_category=None,text='Busy',user="Default"):
        self.category = category
        self.text = text
        self.year = time_submitted.year
        self.month = time_submitted.month
        self.week = time_submitted.strftime("%U")
        self.day = time_submitted.day
        self.hour = time_submitted.hour
        self.minute = time_submitted.minute
        self.second = time_submitted.second
        self.sub_category = sub_category
        self.day_name = time_submitted.strftime("%A")
        self.time_submitted = (self.year,self.month,self.week,self.day,self.day_name,self.hour,self.minute,self.second)
        self.user = user
    
    def __str__(self):
        return f"{self.text} was submitted at {self.time_submitted} under category: {self.category} and sub-category: {self.sub_category} by {self.user}"

user_list = os.listdir("Users")

def input_task():
    print("Select User:")
    for i in range(len(user_list)):
        print(f"({i+1}) {user_list[i]}")
    current_user = input("\n")
    if current_user.isdigit():
        current_user = user_list[int(current_user)-1]

    while True:
        category = input("What is the broad category of the task that you are doing: \n\t\t(1)Studying \n\t\t(2)Playing \n\t\t(3)Watching \n\t\t(4)Productivity \n\t\t(5)Miscellaneous \n\t\t(6)Idle\n").title().strip()
        if category == "Studying" or category == "1":
            category = "Studying"
            while True:
                sub_category = eval(input("Which of the following sub-category best suits your current task: \n\t\t(1)Revision \n\t\t(2)Lectures     \n\t\t(3)Question Practice \n\t\t(4)Work Completion \n\t\t(5)Other\n").title().strip())
                if sub_category in {"Revision","Lectures","Question Practice","Work Completion","Other",1,2,3,4,5}:
                    if type(sub_category) == int:
                        sub_category_number = sub_category
                        sub_category_list = ["Revision","Lectures","Question Practice","Work Completion","Other"]
                        sub_category = sub_category_list[sub_category_number-1]
                    break
                else:
                    print("Enter a valid sub-category")
                    time.sleep(1)
            break
        
        elif category == "Playing" or category == "2":
            category = "Playing"
            while True:
                sub_category = eval(input("Which of the following sub-category best suits your current task: \n\t\t(1)Playing Alone \n\t\t(2)Playing with Friends\n").title().strip())
                if sub_category in {"Playing Alone","Playing With Friends",1,2}:
                    if type(sub_category) == int:
                        sub_category_number = sub_category
                        sub_category_list = ["Playing Alone","Playing With Friends"]
                        sub_category = sub_category_list[sub_category_number-1]
                    
                    break
                else:
                    print("Enter a valid sub-category")
                    time.sleep(1)
            break
        elif category == "Watching" or category == "3":
            category = "Watching"
            while True:
                sub_category = eval(input("Which of the following sub-category best suits your current task: \n\t\t(1)Anime \n\t\t(2)YouTube \n\t\t(3)Movie/TV Show\n").title().strip())
                if sub_category in {"Anime","YouTube","Movie/TV Show",1,2,3}:
                    if type(sub_category) == int:
                        sub_category_number = sub_category
                        sub_category_list = ["Anime","YouTube","Movie/TV Show"]
                        sub_category = sub_category_list[sub_category_number-1]
                    break
                else:
                    print("Enter a valid sub-category")
                    time.sleep(1)
            break
        elif category == "Productivity" or category == "4":
            category = "Productivity"
            while True:
                sub_category = eval(input("Which of the following sub-category best suits your current task: \n\t\t(1)Coding \n\t\t(2)Planning \n\t\t(3)Learning \n\t\t(4)Other\n").title().strip())
                if sub_category in {"Coding","Planning","Learning","Other",1,2,3,4}:
                    if type(sub_category) == int:
                        sub_category_number = sub_category
                        sub_category_list = ["Coding","Planning","Learning","Other"]
                        sub_category = sub_category_list[sub_category_number-1]
                    break
                else:
                    print("Enter a valid sub-category")
                    time.sleep(1)
            break
        elif category == "Miscellaneous" or category == "5":
            category = "Miscellaneous"
            sub_category = input("Which sub-category best suits your current task\n").title().strip()
            break
        elif category == "Idle" or category == "6":
            category = "Idle"
            sub_category = "N/A"
            break
        else:
            print("Please enter a valid category")
            time.sleep(1)
        
    short_task = input("Please describe the task you are doing in short: ")
    current_task = task(datetime.now(),category,sub_category,short_task,current_user)
    return current_task
    


def store(new_task: task):

    user_store  = new_task.user
    store_info = {new_task.day_name:{f"{new_task.hour}-{new_task.minute}":{"Category": new_task.category, "Sub_Category": new_task.sub_category, "Task": new_task.text}}}

    with open(rf"Users\{user_store}\storage.json", "r") as file:
        info = json.load(file)
        if info[f"{new_task.year}-{new_task.week}"]:
            if info[f"{new_task.year}-{new_task.week}"][new_task.day_name]:
                info[f"{new_task.year}-{new_task.week}"][new_task.day_name][f"{new_task.hour}-{new_task.minute}"] = store_info[new_task.day_name][f"{new_task.hour}-{new_task.minute}"]
            else:
                info[f"{new_task.year}-{new_task.week}"][new_task.day_name] = store_info[new_task.day_name]
        else:
            info[f"{new_task.year}-{new_task.week}"] = store_info
        if info["temp"]:
            del info["temp"]
    with open(rf"Users\{user_store}\storage.json", 'w') as file:
        json.dump(info, file, indent=3)

    return
    

if __name__ == "__main__":
    store(input_task())