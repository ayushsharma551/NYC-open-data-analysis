NYC Open Data Pipeline
This project demonstrates an end-to-end data pipeline for ingesting, processing, analyzing, and visualizing NYC 311 service request data using Python, BigQuery, Airflow, and Tableau.

🚀 Project Overview
This pipeline fetches data from the NYC Open Data API, loads it into Google BigQuery, and automates the ingestion process using Apache Airflow. The data is then analyzed using SQL and visualized in Tableau.

📌 Features
REST API Integration: Fetches real-time NYC 311 service requests.
Google BigQuery Storage: Stores structured data for efficient querying.
SQL Aggregations: Analyzes complaint trends, peak hours, borough-wise distribution, and resolution times.
Airflow Automation: Ensures daily ingestion of new data.
Tableau Visualization: Provides an interactive dashboard for insights.
 
Future Enhancements
Implement data validation before loading into BigQuery.
Set up alerts in Airflow for ingestion failures.
Enhance Tableau dashboards with real-time streaming updates.
Optimize SQL queries for faster performance.
