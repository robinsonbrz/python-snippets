import csv
from datetime import datetime

path = "Google Stock Market Data.csv"
file = open(path, newline='')
reader = csv.reader(file, delimiter=";")

header = next(reader) # The first line is the header

data = []

for row in reader:
    # row = [Date, Open, High, Low, Close, Adj. Close]
    date = datetime.strptime(row[0], '%d/%m/%Y')
    open_price = float(row[1]) # ‘open’ is a builtin function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[2])
    
    data.append([date, open_price, high, low, close, volume,
                adj_close])

print (data[0])

return_path = "google_returns.csv"

file = open(return_path, "w")
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i + 1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = round((todays_price - yesterdays_price) / yesterdays_price, 2)
    formatted_date = todays_date.strftime('%d/%m/%Y')
    writer.writerow([formatted_date, daily_return])
    
