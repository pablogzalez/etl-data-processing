# Dockerfile para construir la imagen de Airflow
FROM apache/airflow:2.4.1-python3.9

# Instalamos las dependencias necesarias
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir \
    apache-airflow-providers-postgres \
    pandas \
    Faker \
    apache-airflow-providers-microsoft-azure \
    azure-servicebus

# Creamos los directorios necesarios y establecemos permisos
RUN mkdir -p /opt/airflow/data/input /opt/airflow/data/output \
    && chown -R airflow: /opt/airflow/data

# Copiamos los DAGs y scripts al contenedor
COPY dags/ /opt/airflow/dags/
COPY scripts/ /opt/airflow/scripts/
COPY data/ /opt/airflow/data/

# Establecemos el directorio de trabajo de Airflow
ENV AIRFLOW_HOME=/opt/airflow

# Exponemos el puerto web de Airflow
EXPOSE 8080
