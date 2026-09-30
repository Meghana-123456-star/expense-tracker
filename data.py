import json
import os


DATA_FOLDER = "data"
EXPENSES_FILE = os.path.join(DATA_FOLDER, "expenses.json")


def create_data_file():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "w") as file:
            json.dump([], file, indent=4)


def load_expenses():
    create_data_file()

    with open(EXPENSES_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    create_data_file()

    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=4)