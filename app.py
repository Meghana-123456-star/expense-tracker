import streamlit as st
from datetime import date

from data import load_expenses, save_expenses


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)


# -----------------------------
# LOAD DATA
# -----------------------------

expenses = load_expenses()


# -----------------------------
# TITLE
# -----------------------------

st.title("💰 Expense Tracker")

st.write(
    "A simple expense management application using Streamlit and JSON files."
)


# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Choose an option",
    [
        "Dashboard",
        "Add Expense",
        "Expense Report",
        "Expense List"
    ]
)


# ============================================================
# DASHBOARD
# ============================================================

if menu == "Dashboard":

    st.header("🏠 Dashboard")

    total_expenses = len(expenses)

    total_amount = sum(
        expense["amount"]
        for expense in expenses
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Expenses",
            total_expenses
        )

    with col2:
        st.metric(
            "Total Amount",
            f"₹{total_amount:.2f}"
        )

    st.divider()

    if expenses:

        st.subheader("Recent Expenses")

        for expense in expenses[-5:][::-1]:

            st.write(
                f"**{expense['title']}** - "
                f"₹{expense['amount']:.2f}"
            )

            st.write(
                f"Category: {expense['category']} | "
                f"Date: {expense['date']}"
            )

            st.divider()

    else:

        st.info(
            "No expenses added yet."
        )


# ============================================================
# ADD EXPENSE
# ============================================================

elif menu == "Add Expense":

    st.header("➕ Add Expense")

    with st.form("expense_form"):

        title = st.text_input(
            "Expense Title",
            placeholder="Example: Grocery"
        )

        amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=1.0
        )

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Travel",
                "Education",
                "Shopping",
                "Bills",
                "Health",
                "Entertainment",
                "Other"
            ]
        )

        expense_date = st.date_input(
            "Expense Date",
            value=date.today()
        )

        description = st.text_area(
            "Description",
            placeholder="Enter expense details"
        )

        submitted = st.form_submit_button(
            "Add Expense"
        )

        if submitted:

            if not title:

                st.error(
                    "Please enter an expense title."
                )

            elif amount <= 0:

                st.error(
                    "Amount must be greater than zero."
                )

            else:

                new_expense = {
                    "title": title,
                    "amount": amount,
                    "category": category,
                    "date": str(expense_date),
                    "description": description
                }

                expenses.append(
                    new_expense
                )

                save_expenses(expenses)

                st.success(
                    "Expense added successfully!"
                )


# ============================================================
# EXPENSE REPORT
# ============================================================

elif menu == "Expense Report":

    st.header("📊 Expense Report")

    if not expenses:

        st.info(
            "No expenses available."
        )

    else:

        categories = {}

        for expense in expenses:

            category = expense["category"]

            categories[category] = (
                categories.get(category, 0)
                + expense["amount"]
            )

        st.subheader("Category-wise Expenses")

        for category, amount in categories.items():

            st.write(
                f"**{category}:** ₹{amount:.2f}"
            )

        st.divider()

        total_amount = sum(
            expense["amount"]
            for expense in expenses
        )

        st.subheader("Total Expense")

        st.write(
            f"### ₹{total_amount:.2f}"
        )


# ============================================================
# EXPENSE LIST
# ============================================================

elif menu == "Expense List":

    st.header("📋 Expense List")

    if not expenses:

        st.info(
            "No expenses added yet."
        )

    else:

        for index, expense in enumerate(
            expenses,
            start=1
        ):

            st.subheader(
                f"{index}. {expense['title']}"
            )

            st.write(
                f"**Amount:** ₹{expense['amount']:.2f}"
            )

            st.write(
                f"**Category:** {expense['category']}"
            )

            st.write(
                f"**Date:** {expense['date']}"
            )

            st.write(
                f"**Description:** "
                f"{expense['description']}"
            )

            st.divider()