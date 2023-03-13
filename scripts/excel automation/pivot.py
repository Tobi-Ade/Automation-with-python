import pandas as pd 

data = pd.read_excel("../../data/supermarket_sales.xlsx")
df = data.copy()
df = df[['Gender', 'Product line', 'Total']]

pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round()

pivot_table.to_excel('pivot_table.xlsx', sheet_name='Report', startrow=4)