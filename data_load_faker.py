import pymysql
from faker import Faker
import random
from datetime import datetime

# Step 1: Setup Faker and DB connection
fake = Faker()
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',        # Change if needed
    database='test'         # Make sure 'test' DB exists
)
cursor = conn.cursor()

# Step 2: Define status options
statuses = ['shipped', 'pending', 'cancelled', 'delivered']

# Step 3: Insert 1000 fake orders
for _ in range(1000):
    name = fake.name()
    status = random.choice(statuses)
    amount = round(random.uniform(100, 5000), 2)
    created_at = fake.date_time_this_year()

    cursor.execute("""
        INSERT INTO orders (customer_name, order_status, order_amount, created_at)
        VALUES (%s, %s, %s, %s)
    """, (name, status, amount, created_at))

# Step 4: Commit and close
conn.commit()
cursor.close()
conn.close()

print("✅ Inserted 1000 fake records into 'orders' table.")
