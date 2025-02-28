import requests
import pandas as pd
from google.cloud import bigquery

# Define the API endpoint
url = 'https://data.cityofnewyork.us/resource/erm2-nwe9.json'

# Set parameters (optional, e.g., to limit data or for specific filtering)
params = {
    # You can add filtering here, for example to limit the rows returned.
    # '$limit': 1000,  # Fetch first 1000 rows, for example
}

# Send a GET request to the API endpoint
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Convert the JSON response to a DataFrame
    data = response.json()
    df = pd.DataFrame(data)

    # Rename columns to make them BigQuery-compatible (replace ':' and '@' with underscores)
    df.columns = df.columns.str.replace(":", "_", regex=False)  # Replace colons with underscores
    df.columns = df.columns.str.replace("@", "", regex=False)   # Remove '@' characters

    # Set up BigQuery client
    client = bigquery.Client()

    # Specify your BigQuery dataset and table name
    dataset_id = 'dataanalysis-452323.NYCOpenData'  # Replace with your project and dataset
    table_id = f'{dataset_id}.nyc'  # Replace with your table name

    # Upload the DataFrame to BigQuery
    try:
        # Create job configuration (Optional: define schema or other options)
        job_config = bigquery.LoadJobConfig(
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,  # To append to an existing table
            autodetect=True  # Automatically detect schema if not predefined
        )

        # Upload data to the BigQuery table
        job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
        job.result()  # Wait for the job to complete
        print(f"Data successfully uploaded to {table_id}")
    except Exception as e:
        print(f"Error while uploading to BigQuery: {e}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
