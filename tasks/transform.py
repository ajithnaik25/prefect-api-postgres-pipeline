from prefect import task, get_run_logger


@task(name="transform-data")
def transform(data):
    logger = get_run_logger()

    logger.info("Starting transformation")

    try:
        result = [
            {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"]
            }
            for user in data
        ]

        logger.info(f"Transformed {len(result)} records")
        return result

    except Exception as e:
        logger.error(f"Error in transform: {str(e)}")
        raise
