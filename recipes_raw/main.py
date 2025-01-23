import pandas as pd
from tabulate import tabulate


dataset = pd.read_json("C:\\My Files\\Personal Projects\Recipe Generator\\recipes_raw\\recipes_raw_nosource_ar.json")
df = pd.DataFrame(dataset.head())
print(tabulate(df, headers='keys', tablefmt='psql'))