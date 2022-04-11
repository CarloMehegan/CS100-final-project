# CS100 final project
# Spotify@Russia

#this script creates a wordcloud using all files for the 9 bordering countries
#must specify end date on line 11

countries = ['Belarus', 'Estonia', 'Finland', 'Kazakhstan', 'Latvia', 'Lithuania', 'Norway', 'Poland', 'Ukraine']
other = ['Global', 'USA', 'Russia'] #Russia playlist is now unavailable!
start_date = 40822
day_increment = 100
end_date = 41122

import pandas as pd
genres = ""
for c in countries:
    for i in range(start_date, end_date+1, day_increment):
        file_name = ("0" + str(i) + " " + str(c) + ".csv") # format: "040822 Belarus.csv"
        try:
            data = pd.read_csv(file_name, dtype="string")
            s = ""
            for i in data.Genres.values:
                if str(i) == "<NA>":
                    pass
                else:
                    word = i.replace(" ", "")
                    s = s + word + "\n"
            genres = genres + "\n" + s
        except:
            print("file not found:", file_name)


from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(collocations = False).generate(genres)
plt.figure(figsize=[10,10])
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
