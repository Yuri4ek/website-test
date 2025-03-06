import sqlite3

conn = sqlite3.connect('ram_modules.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS ram_modules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    memory_type TEXT NOT NULL,
    capacity_gb INTEGER NOT NULL,
    speed_mhz INTEGER,
    latency TEXT,
    price REAL NOT NULL,
    currency TEXT NOT NULL
);
''')
conn.commit()


ram_modules = [
    {"name": "Kingston DDR3 4GB", "memory_type": "DDR3", "capacity_gb": 4, "speed_mhz": 1600, "latency": "CL11", "price": 20.99, "currency": "USD"},
    {"name": "Corsair DDR4 16GB", "memory_type": "DDR4", "capacity_gb": 16, "speed_mhz": 3200, "latency": "CL16", "price": 79.99, "currency": "USD"},
    {"name": "G.Skill DDR5 32GB", "memory_type": "DDR5", "capacity_gb": 32, "speed_mhz": 6000, "latency": "CL30", "price": 199.99, "currency": "USD"}
]

for ram in ram_modules:
    cursor.execute('''
    INSERT INTO ram_modules (name, memory_type, capacity_gb, speed_mhz, latency, price, currency)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (ram["name"], ram["memory_type"], ram["capacity_gb"], ram["speed_mhz"], ram["latency"], ram["price"], ram["currency"]))

conn.commit()
cursor.close()
conn.close()
