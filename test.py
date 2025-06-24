import pandas as pd

sales = {"user_id": ["HR51", "UP16", "25BH"], "Rto_": [143000, 148000, 35000]}

sales_df = pd.DataFrame(sales)

print(sales_df)
print(sales_df.sort_values(by="Rto_", ascending=False))
