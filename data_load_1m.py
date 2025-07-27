import mysql.connector
import random
from datetime import datetime, timedelta

# DB Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  # Change this
    database="test"   # Change this
)
cursor = conn.cursor()

# Function to generate random date
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Insert 50,000 records
records = []
start_date = datetime.strptime("2023-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2023-12-31", "%Y-%m-%d")

for i in range(1, 1000001):
    order_id = i
    user_id = random.randint(1000, 9999)
    amount = round(random.uniform(10.0, 5000.0), 2)
    created_at = random_date(start_date, end_date)
    records.append((order_id, user_id, amount, created_at))

# Batch Insert
sql = "INSERT INTO orders_normal (order_id, user_id, amount, created_at) VALUES (%s, %s, %s, %s)"
cursor.executemany(sql, records)
conn.commit()

print(f"✅ Inserted {cursor.rowcount} rows successfully!")

# Close connection
cursor.close()
conn.close()
