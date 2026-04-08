from prefect import flow
from datetime import datetime
from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load


@flow(name="etl-flow", flow_run_name=lambda: f"run-{datetime.now().strftime('%d-%m-%y_%H-%M-%S')}")
def etl_pipeline():
    data = extract()
    transformed = transform(data)
    load(transformed)


if __name__ == "__main__":
    etl_pipeline()
