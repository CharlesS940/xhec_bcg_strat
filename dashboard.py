import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data for customers
customers_data = pd.read_csv("clients.csv")

# Sample data for transactions
transactions_data = pd.read_csv('transactions.csv')

# Convert date columns to datetime
customers_data['Last_Purchase_Date'] = pd.to_datetime(customers_data['Last_Purchase_Date'])
transactions_data['date_order'] = pd.to_datetime(transactions_data['date_order'])

st.title("Customer Transactions Dashboard")

# Dropdown for filtering customers by status
status_filter = st.selectbox("Select Customer Status", options=["All"] + list(customers_data['status'].unique()))

# Filter customers based on status
filtered_customers = customers_data if status_filter == "All" else customers_data[customers_data['status'] == status_filter]

st.subheader("Customers Table")
st.dataframe(filtered_customers)

# Dropdown for selecting customer ID
selected_customer = st.selectbox("Select Client ID", options=filtered_customers['client_id'])

# Filter transactions based on selected customer ID
filtered_transactions = transactions_data[transactions_data['client_id'] == selected_customer]

st.subheader("Transactions Table")
st.dataframe(filtered_transactions)

# Plot transactions over time
st.subheader("Transactions Over Time")
fig = px.line(filtered_transactions, x='date_order', y='sales_net', title=f"Transaction History for Customer {selected_customer}")
st.plotly_chart(fig)
