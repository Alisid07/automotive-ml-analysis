# Automotive Industry Performance Prediction (100 Years Analysis)
# Leveraging Machine Learning to Analyze and Forecast the Performance of Major Automotive Giants

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import streamlit as st
import requests
import json
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Create project directories
os.makedirs("data", exist_ok=True)
os.makedirs("models", exist_ok=True)
os.makedirs("notebooks", exist_ok=True)
os.makedirs("scripts", exist_ok=True)

# Define automotive companies and their respective stock symbols
companies = {
    "Tesla": "TSLA",
    "Ford": "F",
    "General Motors": "GM",
    "Toyota": "TM",
    "BMW": "BMW.DE",
    "Volkswagen": "VOW3.DE",
    "Mercedes-Benz": "MBG.DE"
}

# Function to fetch stock data safely
def fetch_stock_data(ticker, company_name, start_date="1925-01-01", end_date=str(datetime.today().date())):
    print(f"Fetching data for {company_name} ({ticker})...")
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if "Adj Close" in data.columns:
            data["Price"] = data["Adj Close"]
        elif "Close" in data.columns:
            data["Price"] = data["Close"]
        else:
            print(f"Skipping {company_name} ({ticker}): No valid price data available.")
            return None  # Skip this company if no valid price data
        data.to_csv(f"data/{ticker}_historical.csv")
        return data
    except Exception as e:
        print(f"Error fetching data for {company_name} ({ticker}): {e}")
        return None

# Load data safely
data_frames = {}

for company_name, ticker in companies.items():
    df = fetch_stock_data(ticker, company_name)
    if df is not None and "Price" in df.columns:  # Ensure valid data
        data_frames[company_name] = df

# Streamlit Dashboard
st.title("Automotive Industry Performance Dashboard")

# Select company for visualization
selected_company = st.selectbox("Select a Company", list(companies.keys()))

def display_stock_data(company):
    if company in data_frames:
        df = data_frames[company]
        st.subheader(f"Stock Price Data for {company}")
        st.line_chart(df["Price"])
        st.subheader("Statistical Summary")
        st.write(df["Price"].describe())
    else:
        st.write("Data not available for the selected company.")

display_stock_data(selected_company)

# Compare Last 20 Years
def plot_last_20_years_dashboard():
    st.subheader("Stock Performance Over the Last 20 Years")
    plt.figure(figsize=(12, 6))
    for company, df in data_frames.items():
        if df.empty or "Price" not in df.columns:
            continue
        df_last_20 = df[df.index >= "2004-01-01"]
        plt.plot(df_last_20.index, df_last_20["Price"], label=company)
    plt.xlabel("Year")
    plt.ylabel("Stock Price")
    plt.legend()
    st.pyplot(plt)

plot_last_20_years_dashboard()

# Correlation Heatmap
def plot_correlation_heatmap_dashboard():
    st.subheader("Stock Price Correlation Between Companies")
    combined_data = pd.DataFrame()
    for company, df in data_frames.items():
        if df.empty or "Price" not in df.columns:
            continue
        combined_data[company] = df["Price"]
    combined_data.dropna(inplace=True)
    plt.figure(figsize=(10, 6))
    sns.heatmap(combined_data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(plt)

plot_correlation_heatmap_dashboard()

# Save Model
import joblib
joblib.dump(data_frames, "models/stock_data.pkl")

st.write("Dashboard successfully loaded with stock insights and analytics!")
