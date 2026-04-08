from prefect import task, get_run_logger
import requests
from config.config import API_URL


@task(name="extract-data", retries=3, retry_delay_seconds=5)
def extract():
    logger = get_run_logger()

    logger.info("Starting API call")

    try:
        response = requests.get(API_URL)

        if response.status_code != 200:
            raise Exception(f"API failed with status {response.status_code}")

        data = response.json()
        logger.info(f"Fetched {len(data)} records")

        return data

    except Exception as e:
        logger.error(f"Error in extract: {str(e)}")
        raise
