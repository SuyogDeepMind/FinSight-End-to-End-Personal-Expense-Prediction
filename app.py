import streamlit as st
import pandas as pd
import joblib

# Load your trained Ridge model
model = joblib.load("ridge_model.pkl")

# Set page configuration
st.set_page_config(page_title="💸 FinSight – Intelligent Personal Expense Predictor", layout="centered")

# Title and description
st.title("💸 FinSight – Intelligent Personal Expense Predictor 💸")
st.markdown("""
Welcome to the 💸 FinSight – Intelligent Personal Expense Predictor App!  
Enter your monthly financial details to get an estimate of your total personal expenses.
""")

# Sidebar inputs
st.sidebar.header("📊 Input Your Financial Data")
annual_income = st.sidebar.slider("Annual Income (₹)", 100000, 5000000, 500000)
emi = st.sidebar.slider("Monthly EMI (₹)", 0, 100000, 5000)
grocery = st.sidebar.slider("Monthly Grocery Expense (₹)", 1000, 30000, 5000)
food_outside = st.sidebar.slider("Food Outside Expense (₹)", 0, 20000, 1000)
rent = st.sidebar.slider("Monthly Rent (₹)", 0, 100000, 15000)

# Create DataFrame for prediction
input_df = pd.DataFrame({
    'Annual_Income': [annual_income],
    'EMI': [emi],
    'Grocery': [grocery],
    'Food_Outside': [food_outside],
    'Rent': [rent]
})

# Predict total expenses
if st.button("🔍 Predict My Monthly Expenses"):
    prediction = model.predict(input_df)[0]
    st.success(f"🎯 Estimated Monthly Expense: ₹{round(prediction, 2):,}")

# Footer
st.markdown(
    """
    <h1 style='text-align: center; color: #4B8BBE;'>Personal Expense Predictor 💸</h1>
    <h4 style='text-align: center; color: gray;'>Powered with ❤️ by <span style='color:#FF4B4B;'>Suyog Manke</span></h4>
    """,
    unsafe_allow_html=True
)