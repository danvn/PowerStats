import pandas as pd
import math

df = pd.read_csv("Seasons_Stats.csv")

for year in df["Year"]:
    if math.isnan(year):
        continue
    else:
        year = int(year)
        df.loc[df["Year"] == year, "Year"] = f"{year}-01-01T01:00:00.0"

df.to_csv("fixed_years.csv")
