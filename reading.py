# CS100 final project
# Spotify@Russia








import pandas as pd
data = pd.read_csv("040822 Belarus.csv", dtype="string")
# s = data.Series(['a', 'b', 'c'], dtype="string")
# print(data.Artist)

s = data.Genres.values
print(s[3])

# print(data.iloc[0].values[4])

s = ""
for i in data.Genres.values:
    if str(i) == "<NA>":
        pass
    else:
        word = i.replace(" ", "")
        s = s + word + "\n"
print(s)





import nltk

nltk.download('stopwords')

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

# dost = open('crime_and_punishment.txt', 'r', encoding = 'UTF-8') 
# cp = dost.read()
# dost.close()
wordcloud = WordCloud(collocations = False).generate(s)
plt.figure(figsize=[10,10])
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
