from faker import Faker
import psycopg2
import random

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)
cur = conn.cursor()

fake = Faker()

# Генеруємо користувачів
for _ in range(5):
    fullname = fake.name()
    email = fake.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Зберігаємо зміни
conn.commit()

# Генеруємо завдання
for _ in range(10):
    title = fake.text(max_nb_chars=50)
    description = fake.text()
    status_id = random.randint(1, 3)  # Вибираємо випадковий статус
    user_id = random.randint(1, 5)  # Вибираємо випадкового користувача
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id))

# Зберігаємо зміни
conn.commit()

# Закриваємо з'єднання
cur.close()
conn.close()
