import sqlite3

# Данные о модулях оперативной памяти
ram_data = [
    # DDR3
    ("Kingston ValueRAM DDR3 8GB 1600MHz", "DDR3", 8, 1600, 35.00, "USD"),
    ("Crucial DDR3 4GB 1333MHz", "DDR3", 4, 1333, 25.00, "USD"),
    ("G.Skill Ripjaws DDR3 16GB 1866MHz", "DDR3", 16, 1866, 60.00, "USD"),
    ("Corsair Vengeance DDR3 8GB 1600MHz", "DDR3", 8, 1600, 38.00, "USD"),
    ("Patriot Viper DDR3 4GB 1600MHz", "DDR3", 4, 1600, 22.00, "USD"),
    ("Team Elite DDR3 8GB 1333MHz", "DDR3", 8, 1333, 30.00, "USD"),
    ("HyperX Fury DDR3 16GB 1866MHz", "DDR3", 16, 1866, 65.00, "USD"),
    ("ADATA XPG DDR3 8GB 1600MHz", "DDR3", 8, 1600, 36.00, "USD"),
    ("Mushkin Enhanced DDR3 4GB 1333MHz", "DDR3", 4, 1333, 20.00, "USD"),
    ("PNY Performance DDR3 16GB 1600MHz", "DDR3", 16, 1600, 58.00, "USD"),
    ("GeIL EVO DDR3 8GB 1866MHz", "DDR3", 8, 1866, 40.00, "USD"),
    ("OWC DDR3 4GB 1066MHz", "DDR3", 4, 1066, 18.00, "USD"),
    ("Transcend DDR3 8GB 1600MHz", "DDR3", 8, 1600, 34.00, "USD"),
    ("Silicon Power DDR3 16GB 1333MHz", "DDR3", 16, 1333, 55.00, "USD"),
    ("Kingston HyperX DDR3 8GB 1866MHz", "DDR3", 8, 1866, 42.00, "USD"),
    # DDR4
    ("Corsair Vengeance LPX DDR4 16GB 3200MHz", "DDR4", 16, 3200, 45.00, "USD"),
    ("Crucial Ballistix DDR4 8GB 2666MHz", "DDR4", 8, 2666, 30.00, "USD"),
    ("G.Skill Trident Z DDR4 32GB 3600MHz", "DDR4", 32, 3600, 110.00, "USD"),
    ("Kingston Fury Renegade DDR4 16GB 3000MHz", "DDR4", 16, 3000, 48.00, "USD"),
    ("Team T-Force Vulcan DDR4 8GB 3200MHz", "DDR4", 8, 3200, 32.00, "USD"),
    ("Patriot Viper Steel DDR4 32GB 3600MHz", "DDR4", 32, 3600, 105.00, "USD"),
    ("HyperX Fury DDR4 16GB 2666MHz", "DDR4", 16, 2666, 44.00, "USD"),
    ("ADATA XPG Spectrix DDR4 8GB 3000MHz", "DDR4", 8, 3000, 35.00, "USD"),
    ("PNY XLR8 DDR4 32GB 3200MHz", "DDR4", 32, 3200, 100.00, "USD"),
    ("GeIL Orion DDR4 16GB 3600MHz", "DDR4", 16, 3600, 50.00, "USD"),
    ("Mushkin Redline DDR4 8GB 3000MHz", "DDR4", 8, 3000, 33.00, "USD"),
    ("Corsair Dominator Platinum DDR4 32GB 4000MHz", "DDR4", 32, 4000, 150.00, "USD"),
    ("G.Skill Ripjaws V DDR4 16GB 3200MHz", "DDR4", 16, 3200, 46.00, "USD"),
    ("Team Elite DDR4 8GB 2666MHz", "DDR4", 8, 2666, 28.00, "USD"),
    ("Silicon Power Turbine DDR4 32GB 3000MHz", "DDR4", 32, 3000, 95.00, "USD"),
    # DDR5
    ("Kingston Fury Beast DDR5 16GB 5600MHz", "DDR5", 16, 5600, 75.00, "USD"),
    ("Corsair Vengeance DDR5 32GB 6000MHz", "DDR5", 32, 6000, 130.00, "USD"),
    ("TeamGroup T-Force Delta DDR5 8GB 4800MHz", "DDR5", 8, 4800, 50.00, "USD"),
    ("G.Skill Trident Z5 RGB DDR5 16GB 6400MHz", "DDR5", 16, 6400, 90.00, "USD"),
    ("Crucial Pro DDR5 32GB 6000MHz", "DDR5", 32, 6000, 125.00, "USD"),
    ("Patriot Viper Xtreme DDR5 16GB 6200MHz", "DDR5", 16, 6200, 85.00, "USD"),
    ("ADATA Lancer DDR5 8GB 5200MHz", "DDR5", 8, 5200, 55.00, "USD"),
    ("PNY Performance DDR5 32GB 5600MHz", "DDR5", 32, 5600, 120.00, "USD"),
    ("Corsair Dominator Platinum DDR5 16GB 7200MHz", "DDR5", 16, 7200, 140.00, "USD"),
    ("Kingston Fury Impact DDR5 8GB 4800MHz", "DDR5", 8, 4800, 52.00, "USD"),
    ("Team T-Force Vulcan DDR5 32GB 6000MHz", "DDR5", 32, 6000, 128.00, "USD"),
    ("G.Skill Ripjaws S5 DDR5 16GB 5600MHz", "DDR5", 16, 5600, 78.00, "USD"),
    ("Mushkin Proline DDR5 8GB 5200MHz", "DDR5", 8, 5200, 53.00, "USD"),
    ("Silicon Power DDR5 32GB 6400MHz", "DDR5", 32, 6400, 135.00, "USD"),
    ("HyperX Fury DDR5 16GB 6000MHz", "DDR5", 16, 6000, 82.00, "USD"),
]

# Подключение к базе данных SQLite
try:
    conn = sqlite3.connect('components.db')
    cursor = conn.cursor()

    # Создание таблицы
    """cursor.execute('''
        CREATE TABLE IF NOT EXISTS rammodules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            memory_type TEXT NOT NULL,
            capacity_gb INTEGER NOT NULL,
            speed_mhz INTEGER NOT NULL,
            price REAL NOT NULL,
            currency TEXT NOT NULL
        )
    ''')"""

    # SQL-запрос для вставки данных
    insert_query = '''
        INSERT INTO rammodules (name, memory_type, capacity_gb, speed_mhz, price, currency)
        VALUES (?, ?, ?, ?, ?, ?)
    '''

    # Вставка данных
    cursor.executemany(insert_query, ram_data)

    # Подтверждение изменений
    conn.commit()
    print("Данные успешно записаны в таблицу ram_modules!")

except sqlite3.Error as e:
    print(f"Ошибка при работе с базой данных: {e}")
finally:
    # Закрытие соединения
    if cursor:
        cursor.close()
    if conn:
        conn.close()