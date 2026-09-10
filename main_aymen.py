import pandas as pd

df = pd.read_csv("/Users/aymenakram/Desktop/BME 2315/Module 1/BME2315_Module_1/Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print(header)