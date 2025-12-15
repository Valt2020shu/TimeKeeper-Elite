from datetime import datetime 
import json
class task:
    def __init__(self,time_submitted,category='misc',sub_category=None,text='Busy'):
        self.category = category
        self.text = text
        self.year = time_submitted.year
        self.month = time_submitted.month
        self.week = time_submitted.strftime("%U ")
        self.day = time_submitted.day
        self.hour = time_submitted.hour
        self.minute = time_submitted.minute
        self.second = time_submitted.second
        self.sub_category = sub_category
        self.day_name = time_submitted.strftime("%A")
        self.time_submitted = (self.year,self.month,self.week,self.day,self.day_name,self.hour,self.minute,self.second)
    
    def __str__(self):
        return f"{self.text} was submitted at {self.time_submitted} under category: {self.category} and sub-category: {self.sub_category}"



input_task = task(datetime.today(),'Miscellaneous','Extra','This is a test run so please bear with me')
print(input_task)
print(input_task.__dict__)