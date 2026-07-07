import psycopg2
from psycopg2 import sql

print("🚀 DBBot Challenge Solution - Episode 64\n")

# Connect (use environment variables in real projects)
conn = psycopg2.connect(
    host="localhost",
    dbname="mydb",          # change to your database name
    user="postgres",
    password="your_password"
)
cur = conn.cursor()

# Step 1: Create contacts table
cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        phone TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
print("✅ Table 'contacts' ready")

# Step 2: Insert sample contacts (parameterized)
contacts = [
    ("Alice", "alice@example.com", "0300-1234567"),
    ("Bob", "bob@example.com", "0301-9876543"),
    ("Carol", "carol@example.com", "0302-5555555")
]

for name, email, phone in contacts:
    cur.execute(
        "INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)",
        (name, email, phone)
    )

print(f"✅ Inserted {len(contacts)} contacts")

# Step 3: SELECT all
cur.execute("SELECT * FROM contacts")
rows = cur.fetchall()

print("\n📋 All Contacts:")
for row in rows:
    print(f"  ID: {row[0]} | {row[1]} | {row[2]} | {row[3]}")

# Step 4: UPDATE one contact
cur.execute(
    "UPDATE contacts SET phone = %s WHERE email = %s",
    ("0300-9999999", "alice@example.com")
)
print("✅ Updated Alice's phone number")

# Step 5: DELETE one contact
cur.execute(
    "DELETE FROM contacts WHERE email = %s",
    ("carol@example.com",)
)
print("✅ Deleted Carol")

conn.commit()
print("\n🎉 All operations completed successfully!")

cur.close()
conn.close()
