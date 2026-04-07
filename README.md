# CSV to PostgreSQL ETL Pipeline using Prefect

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Prefect.
It extracts data from a CSV file, transforms it using pandas, and loads it into PostgreSQL with incremental loading support to avoid duplicates.

## Architecture

CSV File → Extract Task → Transform Task → Load Task → PostgreSQL
↓
Prefect Flow
↓
Prefect Worker + UI Monitoring

## Tech Stack

* Python
* Prefect (Workflow Orchestration)
* PostgreSQL (Database)
* Pandas (Data Processing)
* psycopg2 (Database Connector)

## Features

* Modular ETL pipeline (Extract, Transform, Load)
* Workflow orchestration using Prefect
* Scheduling and monitoring via Prefect UI
* Bulk insert using `execute_batch`
* Incremental loading using `ON CONFLICT DO NOTHING`
* Environment-based configuration using `.env`
* Logging and retry mechanism

## Project Structure

```
prefect-csv-db-pipeline/
│
├── flows/
│   └── csv_to_postgres_flow.py
│
├── tasks/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── config/
│   └── config.py
│
├── data/
│   └── users.csv
│
├── .env
├── requirements.txt
└── README.md
```

## How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Setup environment variables

Create a `.env` file:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=etl_db
DB_USER=postgres
DB_PASSWORD=your_password
```

### 3. Start Prefect server

```
prefect server start
```

### 4. Set API URL (PowerShell)

```
$env:PREFECT_API_URL="http://127.0.0.1:4200/api"
```

### 5. Create work pool

```
prefect work-pool create default-pool -t process
```

### 6. Start worker

```
prefect worker start --pool default-pool
```

### 7. Deploy flow

```
prefect deploy
```

### 8. Run from UI

Open: http://127.0.0.1:4200
Go to Deployments → Click **Run**

## Sample Output

After running the pipeline:

| name       | email                                       | age | city     |
| ---------- | ------------------------------------------- | --- | -------- |
| John Doe   | [john@example.com](mailto:john@example.com) | 28  | New York |
| Jane Smith | [jane@example.com](mailto:jane@example.com) | 32  | London   |

## What I Learned

* Building end-to-end ETL pipelines
* Workflow orchestration concepts (server, worker, deployment)
* Handling duplicate data using database constraints
* Writing idempotent pipelines
* Debugging real-world pipeline issues

## Future Improvements

* Integrate PySpark for large-scale data processing
* Implement timestamp-based incremental loading
* Deploy pipeline to cloud (AWS/Azure)
* Add data validation checks