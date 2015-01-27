from factual import Factual
import pandas as pd
import os

# factual API credentials
factual = Factual(os.environ["FACTUAL_KEY"], os.environ["FACTUAL_SECRET"])
tbl = factual.table('products')

data = []
for cat in ["Pet Care", "Frozen Foods", "Hair Shampoo", "Soda"]:
    q = tbl.filters({"category": cat })
    for i in range(1, 15):
        q = q.page(2)
        data = data + q.data()

df = pd.DataFrame(data)
# df.to_csv("product_data.csv", index=False)
df[['product_name', 'category']].to_csv("./products.csv", index=False)
