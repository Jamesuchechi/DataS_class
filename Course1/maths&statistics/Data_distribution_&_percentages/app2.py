import pandas as pd

data = {
    'device': ['Mobile', 'Tablet', 'Desktop', 'Mobile', 'Tablet', 'Desktop', 'Mobile', 'Tablet', 'Desktop'],
    'user': [50, 70, 80, 90, 100, 110, 120, 130, 140],
}

df = pd.DataFrame(data)

df['percentage'] = (df['user'] / df['user'].sum()) * 100

print(df)