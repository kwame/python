import csv
from datetime import datetime

path = "/home/kwame/Code/personal/python/functions/google_stock_data.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)
# data = [row for row in reader]

# print(header)
# print(data[0]) 

data = []
for row in reader:
  date = datetime.strptime(row[0], '%m/%d/%Y')
  open_price = float(row[1])
  high = float(row[2])
  low = float(row[3])
  close = float(row[4])
  volume = int(row[5])
  adj_close = float(row[6])

  data.append([date, open_price, high, low, close, volume, adj_close])

print(data[15])

