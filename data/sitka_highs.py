import csv

import seaborn as sns

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

from datetime import datetime


filename = '/home/jimoh1990/data_visualization/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)

    # Get date high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
# print(dates)
# print(highs)

# Plot the high and low temperatures
sns.set(style ='dark')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='blue')
ax.plot(dates, lows, c='red')

# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis='both', which ='major', labelsize=16)

plt.show()
