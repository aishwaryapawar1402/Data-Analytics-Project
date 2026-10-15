# 📊 Data Analytics Project

### 📌 Project Overview
* This is my complete Data Analytics project designed to automate data workflows.
* The script connects to the backend, removes structural errors, handles secure configuration, and outputs statistical reports.
* It ensures all processes are monitored safely using real-time log files.

### 🚀 Tools and Technologies Used
* **SQL:** Used for connecting to the local database file and executing direct data retrieval queries.
* **Python:** Used for filtering records, analytical scripting, mathematical operations, and pipeline automation.
* **Basic Power BI:** Used for converting clean operational tables into basic interactive business dashboards.

### 🛠️ Script Details (Step-by-Step)
* **`ingestion_db.py`**
  * Controls the system's data ingestion pipeline.
  * Safely transfers and saves newly extracted datasets into the core database files.

* **`get_vendor_summary.py`**
  * Connects securely to the storage layer to extract raw data.
  * Pulls active business summaries and vendor performance metrics.
  * 
* **`vendor_performance_analysis.py`**
  * **Basic Config Layer:** Employs a isolated `DB_CONFIG` block at the top to secure database parameters from the core logic.
  * **Anomalies Elimination:** Filters data directly by isolating records where variables are valid (`GrossProfit > 0`, `ProfitMargin > 0`, and `TotalSalesQuantity > 0`).
  * **Data Screening:** Automatically plots boxplots for outlier validation and correlation heatmaps to study field relationships.

# **Log System Configuration:** Uses Python logging with the `force=True` flag to override previous tracks and force successful log creation inside Jupyter environments.
* **File Descriptions (1-by-1):**
  * ingestion_db.log — Tracks dataset changes, column updates, and successful row counts during data ingestion.
  * get_vendor_summary.log — Monitors database query times, system response logs, and connection pings during extraction.
  * vendor_performance.log — Records step-by-step executions of the main analytical engine, tracking rendering operations and script exceptions.
