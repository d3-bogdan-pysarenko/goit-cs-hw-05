from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values
import sys

config = dotenv_values(".env")

try:    
    client = MongoClient(
        f"mongodb+srv://{config['MONGODB_USERNAME']}:{config['MONGODB_PASSWORD']}@cluster0.pp5f01i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        server_api=ServerApi('1')
    )
    db = client.animals
    collection = db.cats
except Exception as e:
    print(f"Помилка з'єднання з базою даних: {e}")
    sys.exit()

def init_db_cats():
    result_many = collection.insert_many(
        [
            {
                "name": "Lama",
                "age": 2,
                "features": ["ходить в лоток", "ловить мишей", "сірий"],
            },
            {
                "name": "barsik",
                "age": 3,
                "features": ["ходить в капці", "дає себе гладити", "рудий"],
            },
            {
                "name": "Liza",
                "age": 4,
                "features": ["ходить в лоток", "не дає себе гладити", "білий"],
            },
            {
                "name": "murka",
                "age": 5,
                "features": ["спить на дивані", "любить рибу", "сірий"]
            },
            {
                "name": "pushok",
                "age": 2,
                "features": [ "мріє стати тигром", "ловить мишей", "білий"]
            }
        ]
    )
    print(result_many.inserted_ids)

# Read
def print_all_records():
    try:
        records = collection.find()
        for record in records:
            print(record)
    except Exception as e:
        print(f"Помилка при виведенні записів: {e}")

def print_cat_info_by_name(cat_name):
    try:
        cat_info = collection.find_one({"name": cat_name})
        if cat_info:
            print(cat_info)
        else:
            print("Кота з таким ім'ям не знайдено.")
    except Exception as e:
        print(f"Помилка при пошуку кота: {e}")

# Update
def update_cat_age(cat_name, new_age):
    try:
        collection.update_one({"name": cat_name}, {"$set": {"age": new_age}})
        print("Вік кота оновлено.")
    except Exception as e:
        print(f"Помилка при оновленні віку: {e}")

def add_feature_to_cat(cat_name, new_feature):
    try:
        collection.update_one({"name": cat_name}, {"$push": {"features": new_feature}})
        print("Нову характеристику успішно додано.")
    except Exception as e:
        print(f"Помилка при додаванні характеристики: {e}")

# Delete
def delete_record_by_name(cat_name):
    try:
        collection.delete_one({"name": cat_name})
        print("Запис про кота видалено.")
    except Exception as e:
        print(f"Помилка при видаленні запису: {e}")

def delete_all_records():
    try:
        collection.delete_many({})
        print("Всі записи в колекції видалено.")
    except Exception as e:
        print(f"Помилка при видаленні всіх записів: {e}")

if __name__ == "__main__":
    while True:
        print("\nМеню:")
        print("1. Створити початкову базу котів")
        print("2. Вивести всі записи")
        print("3. Вивести інформацію про кота за ім'ям")
        print("4. Оновити вік кота")
        print("5. Додати нову характеристику коту")
        print("6. Видалити запис про кота за ім'ям")
        print("7. Видалити всі записи")
        print("0. Вийти")

        choice = input("Введіть номер команди: ")
        if choice == "1":
            init_db_cats()
        elif choice == "2":
            print_all_records()
        elif choice == "3":
            cat_name = input("Введіть ім'я кота: ")
            print_cat_info_by_name(cat_name)
        elif choice == "4":
            cat_name = input("Введіть ім'я кота: ")
            new_age = int(input("Введіть новий вік кота: "))
            update_cat_age(cat_name, new_age)
        elif choice == "5":
            cat_name = input("Введіть ім'я кота: ")
            new_feature = input("Введіть нову характеристику: ")
            add_feature_to_cat(cat_name, new_feature)
        elif choice == "6":
            cat_name = input("Введіть ім'я кота: ")
            delete_record_by_name(cat_name)
        elif choice == "7":
            delete_all_records()
        elif choice == "0":
            break
        else:
            print("Невідома команда. Будь ласка, спробуйте ще раз.")
