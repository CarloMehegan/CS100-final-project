import matplotlib.pyplot as plt
import pandas as pd

def genrePlot(country):
    countries = ['Belarus', 'Estonia', 'Finland', 'Kazakhstan', 'Latvia', 'Lithuania', 'Norway', 'Poland', 'Ukraine']

    while True:
        country = input("What country would you like to analyze?")
        country = country.capitalize()
        if country in countries:
            break
    start_date = 40822
    day_increment = 100
    end_date = 42422

    missingDays = []
    genres = ""
    genreList = []
    occuranceList = []
    dailyOccurances = []

    # Make a list of every genre, and how often they occur
    for i in range(start_date, end_date+1, day_increment):
        file_name = ('0' + str(i) + ' ' + country + '.csv')
        try:
            data = pd.read_csv(file_name, dtype="string")
            s = ""
            for j in data["Genres"].values:
                if str(j) == "<NA>":
                    pass
                else:
                    word = j.replace(" ", "")
                    wordArr = word.split(',')
                    for genre in wordArr:
                        if genre not in genreList: 
                            genreList.append(genre)
                            occuranceList.append(0)
                        else:
                            occuranceList[genreList.index(genre)] += 1
        except:
            print("file not found:", file_name)
            missingDays.append(i)

    # Initial Graph Settings
    fig = plt.figure()
    fig.set_size_inches(20, 15)

    # Making a list of days
    days = []
    for i in range(start_date, end_date+1, day_increment):
        days.append(i)

    # Making a list of the top 10 genres
    topTen = [None] * 10
    for i in range(10):
        topTen[i] = genreList[occuranceList.index(max(occuranceList))]
        genreList.remove(topTen[i])
        del occuranceList[occuranceList.index(max(occuranceList))]

    # Checking how often each genre occurs within the time frame for the country
    for genre in topTen:
        count = [0] * (((end_date-start_date)//100)+1)
        for i in range(start_date, end_date+1, day_increment):
            file_name = ('0' + str(i) + ' ' + country + '.csv')
            try:
                data = pd.read_csv(file_name, dtype="string")
                for j in data["Genres"].values:
                    if str(j) == "<NA>":
                        pass
                    else:
                        word = j.replace(" ","")
                        wordArr = word.split(',')
                        if genre in wordArr:
                            count[(i-start_date)//100] += 1
            except:
                pass
        
        # Removing data for days with no data
        for i in range(len(missingDays)-1, -1, -1):
            del count[(missingDays[i]-start_date)//100]
            try:
                days.remove(missingDays[i])
            except:
                pass
        # Plotting the line for the genre
        plt.plot(days, count, label=genre)

    # Rest of graph settings, including axis labels, title, and proper scaling
    plt.legend(loc='upper left')
    plt.xticks(range(start_date, end_date+1, 100))
    plt.xlabel('Day (MDDYY Format)')
    plt.ylabel('Occurences in top 50 song list')
    plt.title('Occurances of the Top 10 Genres in the Daily Records For ' + country)
    plt.show()

if __name__ == '__main__':
    countries = ['Belarus', 'Estonia', 'Finland', 'Kazakhstan', 'Latvia', 'Lithuania', 'Norway', 'Poland', 'Ukraine']
    while True:
        country = input('What country would you like to analyze? ').lower().capitalize()
        if country in countries:
            break
    genrePlot(country)