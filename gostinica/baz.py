import sqlite3

# Создание базы данных
conn = sqlite3.connect('hotel_database.db')
cursor = conn.cursor()

# Создание таблицы "Клиенты"
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  surname TEXT NOT NULL,
  passport_number TEXT,
  phone_number TEXT,
  email TEXT
);
""")

# Создание таблицы "Номера"
cursor.execute("""
CREATE TABLE IF NOT EXISTS Rooms (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  room_number TEXT NOT NULL,
  type TEXT,
  price REAL,
  available BOOLEAN DEFAULT TRUE
);
""")

# Создание таблицы "Бронирования"
cursor.execute("""
CREATE TABLE IF NOT EXISTS Bookings (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  client_id INTEGER,
  room_id INTEGER,
  check_in_date DATE,
  check_out_date DATE,
  FOREIGN KEY (client_id) REFERENCES Clients(id),
  FOREIGN KEY (room_id) REFERENCES Rooms(id)
);
""")

conn.commit()

# Функция добавления клиента
def add_client(name, surname, passport_number, phone_number, email):
  cursor.execute("""
  INSERT INTO Clients (name, surname, passport_number, phone_number, email)
  VALUES (?, ?, ?, ?, ?)
  """, (name, surname, passport_number, phone_number, email))
  conn.commit()
  print("Клиент добавлен.")

# Функция добавления номера
def add_room(room_number, type, price):
  cursor.execute("""
  INSERT INTO Rooms (room_number, type, price)
  VALUES (?, ?, ?)
  """, (room_number, type, price))
  conn.commit()
  print("Номер добавлен.")

# Функция бронирования номера
def book_room(client_id, room_id, check_in_date, check_out_date):
  cursor.execute("""
  INSERT INTO Bookings (client_id, room_id, check_in_date, check_out_date)
  VALUES (?, ?, ?, ?)
  """, (client_id, room_id, check_in_date, check_out_date))
  conn.commit()
  print("Номер забронирован.")

# Пример использования
add_client("Иван", "Иванов", "1234567890", "88005553535", "ivan.ivanov@email.com")
add_room("101", "Стандартный", 5000)
book_room(1, 1, "2023-12-25", "2023-12-30")

# Закрытие соединения
conn.close()