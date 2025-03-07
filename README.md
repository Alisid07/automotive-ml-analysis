# 🚗 Automotive Industry Performance Prediction (100 Years Analysis)

## 📌 Overview
This project leverages **Machine Learning & Financial Analytics** to analyze and forecast the **performance of major automotive companies** over the last century. The dataset includes **historical stock prices, market trends, and correlations** between major automotive companies, such as:

- **Tesla (TSLA)**
- **Ford (F)**
- **General Motors (GM)**
- **Toyota (TM)**
- **BMW (BMW.DE)**
- **Volkswagen (VOW3.DE)**
- **Mercedes-Benz (MBG.DE)**

This system provides **data visualizations, trend analysis, and predictive modeling** for understanding the automotive industry's performance.

---

## 🎯 **Project Features**
✅ **Stock Data Analysis**: Fetch and visualize stock price data of automotive giants.  
✅ **Interactive Dashboard**: A **Streamlit-powered dashboard** for real-time analytics and visual insights.  
✅ **Trend Analysis**: Compare stock price movements over **the last 20 years**.  
✅ **Correlation Analysis**: Identify relationships between different automotive companies.  
✅ **Machine Learning Prediction**: Train **Linear Regression** models to forecast stock performance.  
✅ **Data Storage & Persistence**: Save data using **joblib** for future analysis.  

---

## 🚀 **Installation Guide**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Alisid07/automotive-ml-analysis.git
cd automotive-ml-analysis
2️⃣ Create and Activate Virtual Environment
sh
Copy
Edit
python -m venv env
# Activate on Windows
env\Scripts\activate
# Activate on macOS/Linux
source env/bin/activate
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Streamlit Dashboard
sh
Copy
Edit
streamlit run Automotive_Ml_Project.py
📊 Data Visualization & Insights
The project includes multiple data visualizations:

📈 Stock Prices Over Time: Compare historical stock trends.
📊 Correlation Heatmap: See how different companies' stocks are correlated.
📉 Last 20 Years Stock Trends: Analyze how automotive companies performed in the past two decades.
📊 Histogram & Scatter Plots: Identify volatility & outliers.
🛠 Tech Stack
Python (pandas, numpy, matplotlib, seaborn, scikit-learn, joblib)
Streamlit (for interactive visualization)
Yahoo Finance API (for stock data retrieval)
Machine Learning Models (Linear Regression for forecasting)
Joblib (for model persistence)
🖥️ Project Structure
bash
Copy
Edit
📂 automotive-ml-analysis/
│-- 📂 data/                 # Folder containing stock price datasets
│-- 📂 models/               # Trained machine learning models
│-- 📂 notebooks/            # Jupyter Notebooks for EDA & Model Training
│-- 📂 scripts/              # Supporting scripts for data collection
│-- env/                     # Virtual environment (excluded in .gitignore)
│-- test_tf.py               # Python script for stock analysis & ML
│-- Automotive_Ml_Project.py # Streamlit app for visualization
│-- requirements.txt         # Python dependencies
│-- README.md                # Project documentation
│-- .gitignore               # Files to ignore in Git
🔧 How It Works
Fetch Stock Data: Uses Yahoo Finance API to collect stock data for selected companies.
Data Preprocessing: Cleans the data, handling missing values.
Exploratory Data Analysis (EDA): Generates key insights using Matplotlib & Seaborn.
Machine Learning Predictions: Implements Linear Regression for price prediction.
Streamlit Dashboard: Displays interactive charts & analytics.
📈 Example Charts
1️⃣ Stock Prices Over Time
This visualization compares stock prices of different companies.

2️⃣ Correlation Heatmap
Displays how strongly the stocks of different companies are correlated.

3️⃣ Last 20 Years Stock Trends
A focused comparison of performance over the past two decades.

👨‍💻 Contributions
Contributions are welcome! Follow these steps:

Fork the Repository on GitHub.
Clone your Forked Repo:
sh
Copy
Edit
git clone https://github.com/YOUR_USERNAME/automotive-ml-analysis.git
Create a New Branch:
sh
Copy
Edit
git checkout -b feature-branch
Make Your Changes and Commit:
sh
Copy
Edit
git add .
git commit -m "Added new visualizations and analytics"
Push to Your Fork:
sh
Copy
Edit
git push origin feature-branch
Create a Pull Request to merge with the main branch.
📜 License
This project is MIT licensed. Feel free to use and modify it as needed.
