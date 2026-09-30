# 💰 Expense Tracker

A simple Expense Tracker application built using Python and Streamlit.

The application allows users to add expenses, categorize expenses, view expense reports, and automatically calculate total expenses.

## 🚀 Features

* Add expenses
* Store expense data using JSON
* Expense categories
* Expense date
* Expense description
* Automatic total expense calculation
* Category-wise expense report
* Dashboard
* Expense list
* No traditional database required

## 🛠️ Technologies Used

* Python
* Streamlit
* JSON
* Git
* GitHub
* Streamlit Community Cloud

## 📁 Project Structure

```text
expense-tracker
│
├── app.py
├── data.py
├── requirements.txt
├── README.md
│
└── data
    └── expenses.json
```

## 💾 Data Storage

This project does not use:

* MySQL
* PostgreSQL
* MongoDB
* SQLite

All expense data is stored in:

```text
data/expenses.json
```

## ▶️ Run Locally

Install Streamlit:

```bash
pip install streamlit
```

Run the application:

```bash
streamlit run app.py
```

## 📊 Expense Calculation

The total expense is calculated using:

```text
Total Expense =
Sum of all expense amounts
```

## 📝 How to Use

### Add Expense

Enter:

* Expense title
* Amount
* Category
* Date
* Description

Then click **Add Expense**.

### Dashboard

View:

* Total number of expenses
* Total amount
* Recent expenses

### Expense Report

View category-wise expense totals.

### Expense List

View all stored expenses.

## ☁️ Deployment

The application can be deployed using Streamlit Community Cloud.

### Deployment Steps

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the `expense-tracker` repository.
5. Select the `main` branch.
6. Select `app.py` as the main file.
7. Click **Deploy**.

## 🎯 Project Objective

This project demonstrates:

* Python programming
* Streamlit
* Form handling
* JSON file handling
* Data processing
* Expense calculations
* Git and GitHub
* Cloud deployment

## 👩‍💻 Author

Meghana

## 📌 Project

**Expense Tracker**

Built with Python + Streamlit + JSON.
