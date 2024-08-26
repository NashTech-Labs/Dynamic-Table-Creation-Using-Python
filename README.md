# Dynamic Table Creation Using Python
This repo code allows you to create tables inside your mysql database with the help of python code. It will also check if the table already exists or not. If a table already present then it will not create a new table inside your database.
## Use Cases
You can use it when you want to share the code with other and other person don't have any schema for tables. The other user only needs to provide the database details and it will deploy all the tables in that database.

## Prerequsites

1. mysql-connector-python==8.3.0

# How to run this project 
## Step 1: clone this repo
## step 2: Install Python modules
```sh
pip3 install -r requirements.txt
```
## step3 : Setup mysql database
If you already have mysql database then you can replace the configuration on step4 and skip this step other wise run this 
```
$ docker run --name cockpitmysql --network host -e MYSQL_ROOT_PASSWORD=my-secret -d mysql
$ docker exec -it cockpitmysql bash
bash-5.1# mysql -u root -p #then enter your password
mysql> create database [your-db-name];
```
## Step 4: Setup All required enviroment variables
```sh

## database configuration environment variables we are using it connection.py
export DBUSER=""
export DBPASSWORD=""
export DBHOST=""
export DBPORT=""
export DBNAME=""
```
# step 5: Run project
```
python3 deployment.py
```