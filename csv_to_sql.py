import os
import pandas as pd
from sqlalchemy import create_engine

# MySQL connection settings
user = 'root'
password = ''
host = 'localhost'
port = 3306
database = 'e_commerce_sales_sql'

# Create SQLAlchemy engine for MySQL
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

# Folder containing CSV files
csv_folder = 'csv_files'

# Loop through CSV files and import them
for filename in os.listdir(csv_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_folder, filename)
        table_name = os.path.splitext(filename)[0]

        # Read CSV
        df = pd.read_csv(file_path)

        # Write to MySQL table
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)

        print(f"✅ Imported '{filename}' into MySQL table '{table_name}'")

print("🎉 All CSV files imported into MySQL successfully!")