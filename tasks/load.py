from prefect import task, get_run_logger
import psycopg2
from psycopg2.extras import execute_batch
from config.config import DB_CONFIG
from config.config import DB_CONFIG, DB_TABLE


@task(name="load-data", retries=3, retry_delay_seconds=5)
def load(data: list):
    logger = get_run_logger()

    if not data:
        logger.warning("No data to insert")
        return

    logger.info("Connecting to database")

    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    try:
        logger.info("Preparing data for insert")

        # Convert list of dict → list of tuples
        records = [
            (item["id"], item["name"], item["email"])
            for item in data
        ]

        logger.info(f"Inserting {len(records)} records")

        query = f"""
            INSERT INTO {DB_TABLE} (id, name, email)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """

        execute_batch(cursor, query, records)

        conn.commit()
        logger.info("Data inserted successfully")

    except Exception as e:
        conn.rollback()
        logger.error(f"Error in load: {str(e)}")
        raise

    finally:
        cursor.close()
        conn.close()
