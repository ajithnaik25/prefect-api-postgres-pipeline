from prefect import task, get_run_logger
import pandas as pd


@task(name="transform-data", retries=2, retry_delay_seconds=5)
def transform(df: pd.DataFrame) -> pd.DataFrame:
    logger = get_run_logger()
    logger.info("Trnasforming the data")

    df = df.dropna()

    df["name"] = df["name"].str.title()
    df["email"] = df["email"].str.lower()
    df["city"] = df["city"].str.title()

    logger.info(f"Transformation is complete. Rows after cleaning: {len(df)}")

    return df
