import pandas as pd
import os

data={'Name': ['Alice', 'Bob', 'Charlie'],
      'Age':  ['20' , '25' , '30'],
      'City': ['New York', 'Luxemborg' , 'England']
    
        
}
df = pd.DataFrame(data)
print(df)

data_dir = 'data'
os.makedirs(data_dir , exist_ok=True)

file_path = os.path.join(data_dir,"samples.csv")

df.to_csv(file_path, index=False)

print(f"CSV file is save to {file_path}")