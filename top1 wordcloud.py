# CS100 final project
# Spotify@Russia

#this script creates a wordcloud using all files for the 9 bordering countries
#wordcloud of just the top #1-10 songs from each chart

#must specify end date on line 14
#must specify range on line 23

countries = ['Belarus', 'Estonia', 'Finland', 'Kazakhstan', 'Latvia', 'Lithuania', 'Norway', 'Poland', 'Ukraine']
other = ['Global', 'USA', 'Russia'] #Russia playlist is now unavailable!
start_date = 40822
day_increment = 100
end_date = 42322

import pandas as pd
genres = ""
for c in countries:
    for i in range(start_date, end_date+1, day_increment):
        file_name = ("0" + str(i) + " " + str(c) + ".csv") # format: "040822 Belarus.csv"
        try:
            data = pd.read_csv(file_name, dtype="string")
            for j in range(0,1): #TODO change this line to pick which range of the chart you want
                song = data["Song"].values[j] 
                song = song.replace(".", "")
                song = song.replace("-", "")
                song = song.replace("(", "")
                song = song.replace(")", "")
                song = song.replace(" ", "")

                genres = genres + "\n" + song
        except:
            print("file not found:", file_name)


from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(collocations = False).generate(genres)
plt.figure(figsize=[10,10])
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
