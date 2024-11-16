import os
import pandas as pd

def save_to_excel(file_path, job_data):
    """Save the scraped job data to an Excel file."""
    # Ensure the directory exists
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create a DataFrame and save it to an Excel file
    df = pd.DataFrame(job_data)
    df.to_excel(file_path, index=False)
    print(f"Job data saved to {file_path}")
