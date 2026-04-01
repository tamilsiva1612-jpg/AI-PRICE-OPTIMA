import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   # for charts

# Title
st.title("AI PriceOptima - Dynamic Pricing System")

# STEP 1: User Input
st.header("Enter Product Details")

price = st.number_input("Current Price", value=50.0)
inventory = st.number_input("Inventory Level", value=100)
discount = st.number_input("Discount", value=10)
competitor = st.number_input("Competitor Price", value=50)

demand_forecast = st.number_input("Demand Forecast", value=100)
units_ordered = st.number_input("Units Ordered", value=50)

# STEP 2: Logic
combined_demand = 0.7 * demand_forecast + 0.3 * units_ordered

predicted_demand = combined_demand
demand_ratio = (predicted_demand - units_ordered) / units_ordered
demand_ratio = np.clip(demand_ratio, -0.2, 0.2)

ml_price = price * (1 + demand_ratio)
ml_revenue = ml_price * predicted_demand

# STEP 3: Output
st.header("Price Recommendation")

st.write("Recommended Price:", round(ml_price, 2))
st.write("Expected Demand:", round(predicted_demand, 2))
st.write("Expected Revenue:", round(ml_revenue, 2))

# STEP 4: Comparison
st.header("Comparison")

original_revenue = price * units_ordered

st.write("Original Price:", price)
st.write("Suggested Price:", round(ml_price, 2))

st.write("Original Revenue:", original_revenue)
st.write("Predicted Revenue:", round(ml_revenue, 2))

improvement = ((ml_revenue - original_revenue) / original_revenue) * 100
st.write("Revenue Improvement (%):", round(improvement, 2))
st.header("KPI Visualization")

# Revenue comparison chart
revenue_data = pd.DataFrame({
    "Type": ["Original", "ML"],
    "Revenue": [original_revenue, ml_revenue]
})

st.bar_chart(revenue_data.set_index("Type"))

# Demand chart
demand_data = pd.DataFrame({
    "Type": ["Units Ordered", "Predicted Demand"],
    "Demand": [units_ordered, predicted_demand]
})

st.bar_chart(demand_data.set_index("Type"))


