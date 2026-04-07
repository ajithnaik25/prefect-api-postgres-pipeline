from prefect import task, get_run_logger
import pandas as pd


@task(name="extract-data", retries=2, retry_delay_seconds=5)
def extract(csv_path: str):
    logger = get_run_logger()
    logger.info(f"Reading the file from: {csv_path}")

    df = pd.read_csv(csv_path)

    logger.info(f"Data extracted successfully. Rows: {len(df)}")

    return df
