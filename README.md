# API to PostgreSQL ETL Pipeline using Prefect

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline that fetches data from a public API, transforms it, and loads it into PostgreSQL.

The pipeline is orchestrated using Prefect with support for retries, logging, and monitoring through the Prefect UI.

## Architecture

API → Extract Task → Transform Task → Load Task → PostgreSQL
↓
Prefect Flow
↓
Prefect Worker + UI Monitoring

## Tech Stack

* Python
* Prefect (Workflow Orchestration)
* PostgreSQL (Database)
* Requests (API calls)
* psycopg2 (Database Connector)

## Features

* API-based data ingestion
* Modular ETL design (Extract, Transform, Load)
* Workflow orchestration using Prefect
* Retry mechanism for API failures
* Bulk insert using `execute_batch`
* Incremental loading using `ON CONFLICT DO NOTHING`
* Environment-based configuration using `.env`
* Logging and error handling

## Project Structure

prefect-api-db-pipeline/
│
├── flows/
│   └── api_to_postgres_flow.py
│
├── tasks/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── config/
│   └── config.py
│
├── .env
├── requirements.txt
└── README.md
```

## API Source

```
https://jsonplaceholder.typicode.com/users
```

## How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Setup environment variables

Create a `.env` file:

API_URL=https://jsonplaceholder.typicode.com/users

DB_HOST=localhost
DB_PORT=5432
DB_NAME=etl_db
DB_USER=postgres
DB_PASSWORD=your_password

DB_TABLE=users
```

### 3. Create Database and Table

```
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150) UNIQUE
);
```

### 4. Start Prefect server

```
prefect server start
```

### 5. Set API URL (PowerShell)

```
$env:PREFECT_API_URL="http://127.0.0.1:4200/api"
```

### 6. Create work pool

```
prefect work-pool create default-pool -t process
```

### 7. Start worker

```
prefect worker start --pool default-pool
```

### 8. Deploy flow

```
prefect deploy
```

### 9. Run from UI

Open: http://127.0.0.1:4200
Go to Deployments → Click **Run**

## Sample Output

After execution:

| id | name          | email                                           |
| -- | ------------- | ----------------------------------------------- |
| 1  | Leanne Graham | [leanne@example.com](mailto:leanne@example.com) |
| 2  | Ervin Howell  | [ervin@example.com](mailto:ervin@example.com)   |

## What I Learned

* Building API-based data ingestion pipelines
* Handling external API failures with retries
* Transforming JSON data into structured format
* Bulk loading data into PostgreSQL
* Implementing incremental loading for idempotent pipelines
* Orchestrating workflows using Prefect

## Future Improvements

* Handle API pagination (large datasets)
* Implement rate limit handling
* Add timestamp-based incremental loading
* Integrate PySpark for large-scale processing
* Deploy pipeline to cloud (AWS/Azure)