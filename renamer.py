#get today's date, and format it
from datetime import date
today = date.today()
formatteddate = today.strftime("%m%d%y")

#replace the "Top 50 - " in the file name, leaving just "041022 Russia" for example
import os
for fileName in os.listdir("."):
    os.rename(fileName, fileName.replace("Top 50 - ", formatteddate + " "))
    # os.rename(fileName, fileName.replace("Top 50 - ", "041622" + " ")) uncomment this line to add a specific date