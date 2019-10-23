# About
Instructions about how to put CEPAGRI dataset into a POSTGRESQL database and then connect a Metabase instance to it, helping the data analysis.

## Install Docker
Instructions: https://docs.docker.com/install/linux/docker-ce/ubuntu/
Post install steps: https://docs.docker.com/install/linux/linux-postinstall/ (“Manage Docker as a non-root user”)

## Install PostgreSQL
Instructions: https://wiki.postgresql.org/wiki/Apt
Packages: postgresql-client pgadmin4

## Install Python libs for development
```shell
sudo apt-get install -y libpq-dev python3-dev 
sudo -H python3 -m pip install setuptools sqlalchemy psycopg2
```

## Create a folder to store the PostgreeSQL database:
```shell
mkdir ~/cepagri-postgres
```

## Run PostgreSQL Docker image:
1. Run:
```shell
docker run --rm  --name cepagri-postgres -e POSTGRES_PASSWORD=123456789 -e POSTGRES_DB=cepagri -d -p 5432:5432 -v ~/cepagri-postgres:/var/lib/postgresql/data postgres
```

## Run Python Notebook to upload the CEPAGRI data to cepagri database
Script: https://github.com/imdavi/climate-health-data-analysis/blob/master/Send%20data%20to%20PostgreSql.ipynb

## Connecting to database
* Credentials
```
Host address: 127.0.0.1 or localhost
Port: 5432
User: postgres
Password: 123456789
```
* Using psql:

```shell
psql -h localhost -U postgres -d postgres -p 5432
```

* Use PGAdmin to query the data easily

## Run Metabase Docker image:
1. Run:
```shell
docker run -d -p 3000:3000 --rm --network host --name metabase metabase/metabase
```
2. Open the address http://localhost:3000 on browser and follow the wizard to configure Metabase
1. Create a PostgreSQL data source using the database credentials
