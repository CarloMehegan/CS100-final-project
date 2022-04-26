import matplotlib.pyplot as plt
import pandas as pd

def graphProperty(prop):
    countries = ['Belarus', 'Estonia', 'Finland', 'Kazakhstan', 'Latvia', 'Lithuania', 'Norway', 'Poland', 'Ukraine']
    properties = ['Dance', 'Energy', 'Acoustic', 'Instrumental', 'Happy', 'Speech']

    while prop not in properties:
        prop = input('What property would you like to analyze?').capitalize()

    # Date Info
    start_date = 40822
    day_increment = 100
    end_date = 42422

    # Graph stuff
    fig, ax = plt.subplots()
    xPos = 0

    # Collect values for the given property every day for each country, take the average, and plot it
    for country in countries:
        xPos += 1
        propSum = 0
        totalCount = 0
        for i in range(start_date, end_date+1, day_increment):
            file_name = ('0' + str(i) + ' ' + country + '.csv')
            try:
                data = pd.read_csv(file_name, dtype="string")
                for j in data[prop].values:
                    propSum += int(j)
                    totalCount += 1
            except:
                pass
        propAvg = propSum/totalCount
        plt.bar(x=xPos, height=propAvg)

    # Formatting the graph and adding labels
    ax.set_xticks(range(1, len(countries)+1))
    ax.set_xticklabels(labels=countries)
    fig.set_size_inches(20, 15)
    plt.title('Average "' + prop + '" Value for Each Country\'s Top 50 During Time Period')
    plt.xlabel('Country')
    plt.ylabel('Average Value')
    plt.show()

if __name__ == '__main__':
    # Takes user input for which property they want to analyze
    prop = input('What property would you like to analyze?').capitalize()
    graphProperty(prop)
