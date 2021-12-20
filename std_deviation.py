import math
import csv

with open("data.csv", newline='') as f:
    graph_data = csv.reader(f)
    data = list(graph_data)

data = data[0]
b = len(data)
sum = 0
for d_sum in data:
    sum += int(d_sum)
    
mean = sum/b


dev_data = []

for n in data :
    a = int(n) - mean
    a = a ** 2
    dev_data.append(a)


dev_sum = 0

for d in dev_data:
    dev_sum += d


deviation = (dev_sum/ b-1)**(1/2)

print(deviation)