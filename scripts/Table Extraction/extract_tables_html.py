import pandas as pd 

tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Sopranos_episodes")

print(f"{len(tables)}")

print(tables[0])
