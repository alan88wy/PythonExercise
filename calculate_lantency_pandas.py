import pandas as pd

df = pd.read_csv("logs.csv", delimiter=' ', index_col=False, header=None, names=['date', 'time', 'user', 'latency'])

"""
Step	        Purpose
groupby('user')	Split the DataFrame into groups by user
['latency']   	Select the latency column within each group
.mean()	Compute mean latency per user
.reset_index()	Turn the result back into a clean DataFrame
.rename(...)	Give the mean column a descriptive name
"""

result = (
    df.groupby('user')['latency']
      .mean()
      .reset_index()
      .rename(columns={'latency': 'average_latency'})
)

for _, row in result.iterrows():
    print(f'User: {row["user"]}, Average Latency: {row["average_latency"]:.2f} ms')
    
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