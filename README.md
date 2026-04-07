# CSV to PostgreSQL ETL Pipeline using Prefect

## Overview

This project demonstrates an end-to-end ETL pipeline built using Prefect.
It extracts data from a CSV file, transforms it using pandas, and loads it into PostgreSQL with incremental loading support.

## Tech Stack

Python
Prefect (Workflow Orchestration)
PostgreSQL (Database)
Pandas (Data Processing)

## Features

Modular ETL pipeline (Extract, Transform, Load)
Prefect flow with scheduling and monitoring
Environment-based configuration using `.env`
Bulk insert using `execute_batch`
Incremental loading using `ON CONFLICT DO NOTHING`
Logging and retries

## Project Structure

```
prefect-csv-db-pipeline/
│
├── flows/
├── tasks/
├── config/
├── data/
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

Create `.env` file:

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

## Key Learnings

Workflow orchestration using Prefect
Handling database operations with PostgreSQL
Building idempotent ETL pipelines
Debugging real-world pipeline issues

## Future Improvements

Add PySpark for large-scale processing
Integrate cloud storage (AWS/Azure)
Implement incremental load using timestamps
