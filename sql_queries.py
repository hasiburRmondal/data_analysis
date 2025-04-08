import pandas as pd
from sqlalchemy import create_engine

db_url = 'mysql+pymysql://root:@localhost:3306/e_commerce_sales_sql'
engine = create_engine(db_url)

# ================ Get State wise customer count / 2nd highest ================
query = """
SELECT DISTINCT customer_state, COUNT(*) AS customer_count
FROM customers
GROUP BY customer_state
ORDER BY customer_count DESC LIMIT 1 OFFSET 1;
"""
statewise_customer_count = pd.read_sql(query, engine)
print("State wise customer count:")
print(statewise_customer_count)