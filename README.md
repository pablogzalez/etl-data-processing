# ETL Data Processing

## Description

This project implements two ETL (Extract, Transform and Load) pipelines to process sales and inventory data using **Apache Airflow**, **PostgreSQL**, **Elasticsearch**, y **Kibana**. It is containerized with **Docker** and orchestrated with **Docker Compose** to facilitate its deployment and management.

## Prerequisites

Before you begin, make sure you have the following components installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Configuration

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/tu-usuario/etl-data-processing.git
cd etl-data-processing/docker
```

### 2. Configure the `.env` File

In the `docker/` directory, create a file called `.env` and define all the necessary environment variables. 

- Generate the Fernet Key:
Ensure you have Python installed, then run the following command in your terminal:
```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```
- This command will output a secure Fernet Key, for example:
```bash
y3u8QzZKk0YhL1t0a9BfZJ3gHk9D3V0YhL1t0a9BfZJ3gHk9D3V0==
```
Below is an example of what the `.env` file should look like:

```bash
# PostgreSQL
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow

# Airflow
AIRFLOW__CORE__EXECUTOR=SequentialExecutor
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:${POSTGRES_PASSWORD}@postgres/${POSTGRES_DB}
AIRFLOW__CORE__FERNET_KEY=your_fernet_key
#default
AIRFLOW__WEBSERVER__SECRET_KEY=my_secret_key
AIRFLOW__WEBSERVER__WORKERS=2
PYTHONPATH=/opt/airflow

# Elasticsearch
ES_JAVA_OPTS=-Xms512m -Xmx512m
DISCOVERY_TYPE=single-node
XPACK_SECURITY_ENABLED=false

# Others
AIRFLOW_USERNAME=user
AIRFLOW_FIRSTNAME=Name
AIRFLOW_LASTNAME=LastName
AIRFLOW_EMAIL=user@example.com
AIRFLOW_PASSWORD=airflow_password

# Ports (you can adjust them if you wish)
ELASTICSEARCH_PORT=9200
KIBANA_PORT=5601
AIRFLOW_WEB_PORT=8081
```
Make sure to change these values according to your configuration.

## Execution

To start the ETL pipelines, follow these steps:

### 1. Start the Docker Containers

Run the following command to build and start all the necessary containers:

```bash
docker-compose up -d
```

Check the status of the containers to ensure they are running correctly:

```bash
docker-compose ps
```

### 2. Access and Configure Airflow

1. **Access the Airflow Web Interface**:

Open your browser and navigate to [http://localhost:8081](http://localhost:8081).

2. **Log In to Airflow**:

Use the credentials defined in your `.env` file:

- **Username**: `user` (as specified by `AIRFLOW_USERNAME`)

- **Password**: `airflow_password` (as specified by `AIRFLOW_PASSWORD`)

3. **Execute the DAGs**:

- Navigate to the **DAGs** section.

- You should see the ETL DAGs listed.

- Toggle the **ON** switch to activate the DAGs.

- Click the **Trigger Dag** button to manually trigger the DAGs or wait for their scheduled runs.

### 3. Configure Kibana

1. **Access Kibana**:

Open your browser and navigate to [http://localhost:5601](http://localhost:5601).

2. **Add Index Patterns**:

- Navigate to **Management** > **Stack Management** > **Kibana*> **Index Patterns**.

- Click on **Create index pattern**.

- Enter the name of the Elasticsearch index you want to visualize (e.g., `sales-*` or `inventory-*`).

- Follow the prompts to complete the index pattern creation.

3. **Visualize Data in Discover**:

- After creating the index patterns, go to the **Discover** section.

- Select the newly created index pattern from the dropdown menu.

- You should now see your processed data available for exploration and analysis.

## Monitoring

Use Kibana to visualize data processed in Elasticsearch. Access Kibana at the following URL:

[http://localhost:5601](http://localhost:5601)

Additionally, you can monitor the logs of your Docker containers to troubleshoot any issues:

```bash
docker-compose logs
```

## Stopping the Services

When you are done, you can stop all containers with:

```bash
docker-compose down
```

## License

This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.

-

### Additional Notes

- **Fernet Key**: Ensure that you generate a secure Fernet key for `AIRFLOW__CORE__FERNET_KEY` to encrypt sensitive data in Airflow.

- **Airflow Secret Key**: Similarly, use a strong secret key for `AIRFLOW__WEBSERVER__SECRET_KEY` to secure the Airflow web interface.

- **Resource Allocation**: Depending on your machine's resources, you might need to adjust the Java options for Elasticsearch (`ES_JAVA_OPTS`) to optimize performance.

- **Persistent Data**: Consider configuring Docker volumes if you want to persist data between container restarts.

Feel free to customize the configuration and steps according to your specific requirements.
