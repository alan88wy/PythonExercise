import csv
from decimal import Decimal, InvalidOperation

data = {}

try:
    with open('logs.csv', mode='r', newline='') as csvfile:
        # If there are column headers, use DictReader instead 
        # and refer to each column like row['usr'], row['latency'], etc.
        reader = csv.reader(csvfile, delimiter=' ')
        
        for row in reader:
            dt, tm, usr, lat_str = row
            
            try:
                latency = Decimal(lat_str)
            except (InvalidOperation, KeyError):
                continue
            
            if usr not in data:
                data[usr] = {
                    'total_latency': Decimal(0),
                    'count': 0
                }
            
            data[usr]['total_latency'] += latency
            data[usr]['count'] += 1
            
except FileNotFoundError:
    print("The file 'logs.csv' was not found.")
        
for usr, stats in data.items():
    if stats['count'] == 0:
        continue
    
    avg_latency = stats['total_latency'] / stats['count']
    print(f'User: {usr}, Average Latency: {avg_latency:.2f} ms')

"""
import pandas as pd 

logs = [
    ["user1", 4.3],
    ["user1", 3.5],
    ["user2", 2.35],
    ["user1", 4.0],
    ["user1", 3.89],
    ["user2", 2.85],
]

df = pd.DataFrame(logs, columns=["user", "latency"])

result = (
    df.groupby(["user"])["latency"]
    .mean()
    .reset_index()
    .rename(columns={'latency': 'average_latency'}))
    
for i, row in result.iterrows():
    print(f"{i+1} - {row.user}, Average Latency: {row.average_latency} ms")
"""