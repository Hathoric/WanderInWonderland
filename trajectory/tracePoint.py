import csv

locations1 = []

with open('day1.csv') as f:
  reader = csv.reader(f)
  next(reader)
  
  for row in reader:
    location = f"{row[1]},{row[2]},0 "
    locations1.append(location)
  
print(",".join(locations1))