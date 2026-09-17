import pandas as pd

df = pd.read_csv("/Users/destinysuarez/Desktop/Computational BME/Module 1/BME2315_Module_1/Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print(header)