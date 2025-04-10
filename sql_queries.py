import pandas as pd
from sqlalchemy import create_engine

db_url = 'mysql+pymysql://root:@localhost:3306/e_commerce_sales_sql'
engine = create_engine(db_url)

# ================ Get State wise customer count / 2nd highest ================
# query = """
# SELECT DISTINCT customer_state, COUNT(*) AS customer_count
# FROM customers
# GROUP BY customer_state
# ORDER BY customer_count DESC LIMIT 1 OFFSET 1;
# """
# statewise_customer_count = pd.read_sql(query, engine)
# print("State wise customer count:")
# print(statewise_customer_count)

# =====================Find the total revenue by month================
# query = """
# SELECT DATE_FORMAT(o.order_purchase_timestamp, '%%Y-%%m') AS month,
#        SUM(p.payment_value) AS total_revenue
# FROM orders o
# INNER JOIN payments p ON o.order_id = p.order_id
# GROUP BY DATE_FORMAT(o.order_purchase_timestamp, '%%Y-%%m')
# ORDER BY total_revenue DESC;
# """
# total_revenue_by_month = pd.read_sql(query, engine)
# print("Total revenue by month:")
# print(total_revenue_by_month)

# =====================Show the top 3 products by total sales================
# query = """
# SELECT p.`product category`, SUM(i.price) AS total_sales
# FROM order_items i
# INNER JOIN products p ON i.product_id = p.product_id
# GROUP BY p.`product category`
# ORDER BY total_sales DESC
# LIMIT 3;
# """
# top_3_categories = pd.read_sql(query, engine)
# print("Top 3 product categories by total sales:")
# print(top_3_categories)

# =====================Month Over Month Sale================
query = """
SELECT DISTINCT
    month,
    total_sales,
    LAG(total_sales) OVER (ORDER BY month) AS previous_month_sales,
    ROUND(
        (total_sales - LAG(total_sales) OVER (ORDER BY month)) /
        LAG(total_sales) OVER (ORDER BY month) * 100,
        2
    ) AS month_over_month_change
FROM (
    SELECT
        DATE_FORMAT(o.order_purchase_timestamp, '%%Y-%%m') AS month,
        SUM(p.payment_value) AS total_sales
    FROM orders o
    INNER JOIN payments p ON o.order_id = p.order_id
    GROUP BY DATE_FORMAT(o.order_purchase_timestamp, '%%Y-%%m')
) AS monthly_sales
ORDER BY month;


"""
month_over_month_sales = pd.read_sql(query, engine)
# month_over_month_sales = month_over_month_sales.drop_duplicates()
print("Month Over Month Sale:")
print(month_over_month_sales)



