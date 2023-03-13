import pandas as pd 
import camelot 

tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Sopranos_episodes")

print(f"{len(tables)}")
