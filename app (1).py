import streamlit as st
import pandas as pd

# Initialize session state for expenses
if "expenses" not in st.session_state:
    st.session_state["expenses"] = pd.DataFrame(columns=["Amount", "Category", "Note"])

st.title("📊 Daily Expense Tracker")

# Input fields
amount = st.number_input("Enter Amount (Whole Number Only)", min_value=0, step=1)
category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
note = st.text_input("Note (Optional)")

# Add Expense Button
if st.button("➕ Add Expense"):
    new_expense = pd.DataFrame([[amount, category, note]], columns=["Amount", "Category", "Note"])
    st.session_state["expenses"] = pd.concat([st.session_state["expenses"], new_expense], ignore_index=True)
    st.success(f"Added: {amount} in {category}")

# Show Table
st.subheader("📋 Expense Records")
st.dataframe(st.session_state["expenses"])

# Show Total Expense
if st.button("💰 Show Total"):
    total = st.session_state["expenses"]["Amount"].sum()
    st.info(f"Total Expenses: {total}")

# Reset Button
if st.button("🗑 Reset All"):
    st.session_state["expenses"] = pd.DataFrame(columns=["Amount", "Category", "Note"])
    st.warning("All expenses reset!")
