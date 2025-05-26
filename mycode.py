import pandas as pd
import os

data={'Name': ['Alice', 'Bob', 'Charlie'],
      'Age':  ['20' , '25' , '30'],
      'City': ['New York', 'Luxemborg' , 'England']
    
        
}
df = pd.DataFrame(data)


new_row_loc ={'Name': 'GF1', 'Age': '19', 'City' : 'NewYork' }
df.loc[len(df.index)]= new_row_loc

new_row_loc1 ={'Name': 'GF2', 'Age': '19', 'City' : 'New Jearsey' }
df.loc[len(df.index)]= new_row_loc1

data_dir = 'data'
os.makedirs(data_dir , exist_ok=True)

file_path = os.path.join(data_dir,"samples.csv")
print(df)
df.to_csv(file_path, index=False)

print(f"CSV file is save to {file_path}")