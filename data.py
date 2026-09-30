import json
import os


# ============================================================
# FILE PATH
# ============================================================

DATA_FOLDER = "data"

EXPENSES_FILE = os.path.join(
    DATA_FOLDER,
    "expenses.json"
)


# ============================================================
# CREATE DATA FILE
# ============================================================

def create_data_file():

    os.makedirs(
        DATA_FOLDER,
        exist_ok=True
    )

    if not os.path.exists(EXPENSES_FILE):

        with open(
            EXPENSES_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )


# ============================================================
# LOAD EXPENSES
# ============================================================

def load_expenses():

    create_data_file()

    try:

        with open(
            EXPENSES_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            if isinstance(data, list):

                return data

            return []

    except (
        json.JSONDecodeError,
        FileNotFoundError
    ):

        return []


# ============================================================
# SAVE EXPENSES
# ============================================================

def save_expenses(expenses):

    create_data_file()

    with open(
        EXPENSES_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            expenses,
            file,
            indent=4
        )