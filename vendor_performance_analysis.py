# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import sqlite3
import logging
from scipy.stats import ttest_ind
import scipy.stats as stats

# Configure logging to monitor program execution steps
logging.basicConfig(
    filename="logs/vendor_performance.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='a',
    force= True
)

# Disable unnecessary warning messages
warnings.filterwarnings('ignore')

# Basic configuration hiding the database file details
DB_CONFIG = {
    "database": "inventory.db"
}

# Connect to the SQLite database
try:
    conn = sqlite3.connect(DB_CONFIG["database"])
    logging.info(f"Database connection successful with {DB_CONFIG['database']}")
except Exception as e:
    logging.error(f"Error connecting to database: {str(e)}")
    raise

# Fetch valid and filtered records from database by removing inconsistencies
try:
    query = """
    SELECT * 
    FROM vendor_sales_summary 
    WHERE GrossProfit > 0 
    AND ProfitMargin > 0 
    AND TotalSalesQuantity > 0
    """
    df = pd.read_sql_query(query, conn)
    logging.info(f"Successfully fetched and filtered {len(df)} valid records from database")
except Exception as e:
    logging.error(f"Error executing filtered query: {str(e)}")
    raise

# Identify numerical columns for analysis
numerical_cols = df.select_dtypes(include=np.number).columns
logging.info(f"Identified numerical columns: {list(numerical_cols)}")

# Plot boxplots for outlier detection
try:
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(numerical_cols):
        plt.subplot(4, 4, i+1)
        sns.boxplot(y=df[col])
        plt.title(col)
    plt.tight_layout()
    plt.show()
    logging.info("Outlier detection boxplots rendered successfully")
except Exception as e:
    logging.error(f"Error plotting boxplots: {str(e)}")

# Plot count plots for top 10 categorical values
try:
    categorical_cols = ["VendorName", "Description"]
    plt.figure(figsize=(12, 5))
    for i, col in enumerate(categorical_cols):
        plt.subplot(1, 2, i+1)
        sns.countplot(y=df[col], order=df[col].value_counts().index[:10])
        plt.title(f"Count Plot of {col}")
    plt.tight_layout()
    plt.show()
    logging.info("Categorical count plots rendered successfully")
except Exception as e:
    logging.error(f"Error plotting count plots: {str(e)}")

# Plot correlation heatmap for numerical features
try:
    plt.figure(figsize=(12, 8))
    correlation_matrix = df[numerical_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()
    logging.info("Correlation heatmap rendered successfully")
except Exception as e:
    logging.error(f"Error plotting heatmap: {str(e)}")

# Close the database connection
conn.close()
logging.info("Database connection closed gracefully")