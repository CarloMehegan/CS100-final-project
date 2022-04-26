# CS100 final project
# Spotify@Russia

#this script compares each country to the global leaderboard
#and makes a bar chart

countries = ['Belarus', 'Estonia', 'Finland', 'Kazakhstan', 'Latvia', 'Lithuania', 'Norway', 'Poland', 'Ukraine', 'USA']
control = 'Global'
start_date = 40822
day_increment = 100
end_date = 42522

import pandas as pd
# ids = ''
# for i in range(start_date, end_date+1, day_increment):
#     file_name = ("0" + str(i) + " " + str(control) + ".csv") # format: "040822 Global.csv"
#     try:
#         data = pd.read_csv(file_name, dtype="string") #read the file
#         s = ""
#         for j in data["Spotify Track Id"].values: #we want every track id
#             if str(i) == "<NA>":
#                 pass
#             else:
#                 s = s + j + " " #add the track id to our list
#         ids = ids + s
#     except:
#         print("file not found:", file_name)


unique_counts = [0] * len(countries) #should be ten countries
for c in countries:
    unique = 0
    for i in range(start_date, end_date+1, day_increment):
        file_name = ("0" + str(i) + " " + str(c) + ".csv") # format: "040822 Belarus.csv"
        control_file = ("0" + str(i) + " " + str(control) + ".csv") # format: "040822 Global.csv"
        try:
            data = pd.read_csv(file_name, dtype="string")
            control_data = pd.read_csv(control_file, dtype="string")
            s = control_data["Spotify Track Id"].values #ids from the global chart of that day
            for j in data["Spotify Track Id"].values: #TODO change this line to use a different column
                if str(j) == "<NA>":
                    pass
                elif j not in s: #if the id is not in the global id that same day, incrment uniqueness
                    unique += 1
        except:
            print("file not found:", file_name)
    unique_counts[countries.index(c)] = unique #put number into list


import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(20, 15)

# x-coordinates of left sides of bars
left = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
 
# heights of bars
# equal to bar_height
 
# labels for bars
tick_label = ['Belarus', 'Estonia', 'Finland', 'Kazak.', 'Latvia', 'Lithu.', 'Norway', 'Poland', 'Ukraine', 'USA']
 
# plotting a bar chart
plt.bar(left, unique_counts, tick_label = tick_label,
        width = 3, color = ['green'])
 
# naming the x-axis
plt.xlabel('countries')
# naming the y-axis
plt.ylabel('unique songs')
# plot title
plt.title('Songs unique to each country (compared to Global chart)')
 
# function to show the plot
plt.show()
