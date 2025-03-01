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

Summary of Results from NYC 311 Complaints Analysis
After analyzing the NYC Open Data on 311 service requests, the following insights were obtained:

1️⃣ Top Complaint Types in NYC
The most frequent complaint types include Noise, Illegal Parking, and Heating Issues.
These complaints highlight key urban challenges such as infrastructure issues and community disputes.
2️⃣ Complaints by Borough
Brooklyn and Manhattan have the highest number of complaints.
This suggests that denser or more active boroughs experience a higher volume of 311 calls.
3️⃣ Peak Complaint Hours
Complaints peak between 6 PM - 10 PM, indicating that issues arise after work hours.
Noise complaints tend to rise significantly at night.
4️⃣ Trends Over Time
There is a seasonal pattern in complaints, with spikes during winter (heating issues) and summer (noise, air conditioning failures).
Complaints gradually increase year-over-year, possibly due to population growth or better accessibility to 311 services.
5️⃣ Submission Channels
Most complaints are submitted via phone calls and online platforms.
Mobile app usage is increasing, indicating a shift toward digital government services.
6️⃣ Average Time to Resolve Complaints
Some complaints (like noise) get resolved within a few hours, while building-related issues take longer.
Complaints related to building inspections, plumbing, and heating take the longest to resolve.
7️⃣ Monthly Complaint Patterns
Certain complaints spike during specific months:
Heating issues peak in December – February.
Noise complaints peak in summer months (June – August).
8️⃣ Borough vs. Complaint Type
Manhattan & Brooklyn: High noise complaints.
Queens & The Bronx: More infrastructure-related issues.
Staten Island: Fewer overall complaints but relatively high property maintenance complaints.
📌 Key Takeaways
Noise and illegal parking dominate complaints—highlighting key areas for city improvement.
Winter and summer bring distinct challenges—heating failures vs. noise and AC breakdowns.
Borough differences suggest different policy needs for each area.
Automating complaint handling via digital platforms could improve response times.

