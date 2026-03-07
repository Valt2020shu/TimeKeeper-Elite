import seaborn as sns
import matplotlib.pyplot as plt
import json
from datetime import datetime 
from input import user_selection
import pandas as pd

sns.set_style("dark")
current_user = user_selection()
with open(rf"Users/{current_user}/storage.json", "r") as file:
    file_info = json.load(file)
with open(rf"Users/{current_user}/preferences.json", "r") as file:
    ideal = json.load(file)["Ideal Time"]

frequency = {"Studying": 0,"Productivity": 0, "Playing": 0, "Watching": 0, "Miscellaneous": 0, "Idle": 0}
time = datetime.now()



for days in file_info[f"{time.year}-{time.strftime("%U")}"].values():
    for hours in days:  
        frequency[days[hours]["Category"]] += 1
chart_data = {"Categories": [], "Hours Spent": [], "Ideal Time":[]}
for i in frequency:
    chart_data["Categories"].append(i)
    chart_data["Hours Spent"].append(frequency[i])
    chart_data["Ideal Time"].append(ideal[i])
    

bar = sns.barplot(data=chart_data, x= "Categories", y = "Hours Spent", hue="Categories")
plt.title(f"{time.year}-{time.strftime("%U")}")
for container in bar.containers:
    bar.bar_label(container)
bar = plt.gcf()
bar.savefig(rf"Users/{current_user}/Summary/{time.year}-{time.strftime("%U")}-Bar.png")
plt.show()

plt.pie(chart_data["Hours Spent"], labels=chart_data["Categories"],autopct='%1.1f%%')
plt.title(f"{time.year}-{time.strftime("%U")}")
pie = plt.gcf()
pie.savefig(rf"Users/{current_user}/Summary/{time.year}-{time.strftime("%U")}-Pie.png")
plt.show()

chart_df = pd.DataFrame(chart_data)

line_1 = sns.lineplot(data=chart_df, x="Categories", y = "Hours Spent", label= "Hours Spent", markers=True, marker="o")
line_2 = sns.lineplot(data=chart_df, x="Categories",y = "Ideal Time", label = 'Ideal Time', markers=True, marker="o")
for i, row in chart_df.iterrows():
    plt.text(i, row['Hours Spent'] + 0.5, f"{row['Hours Spent']}", 
             ha='center', va='bottom', fontweight='bold', color='blue')
    
    plt.text(i, row['Ideal Time'] - 0.5, f"{row['Ideal Time']}", 
             ha='right', va='top', fontweight='bold', color='orange')
plt.title(f"{time.year}-{time.strftime("%U")}")
plt.legend()

line = plt.gcf()

line.savefig(rf"Users/{current_user}/Summary/{time.year}-{time.strftime("%U")}-Line.png")
plt.show()