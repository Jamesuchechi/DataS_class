import pandas as pd

# create a sample DataFrame
data = {
    "Hours_Studied": [1, 2, 3, 4, 5],
    "Test_Score": [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)
print(df.corr())  # Calculate and print the correlation matrix