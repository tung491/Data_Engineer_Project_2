# Data Modeling with Apache Cassandra

## Description
* This database contains the information of users and songs  
* Summarize the csv files in event_data to one csv file
* This database provides the good management to its ower
* Analyse this database can help ower adjust their behavior and products to fit with users

## Schema
* songplay1:
       * sessionId int PRIMARY KEY
       * itemInSession int PRIMARY KEY
       * artist varchar
       * song varchar
       * length float

* songplay2:
    * userId int PARTITION KEY 
    * sessionId int PARTITION KEY
    * artist varchar CLUSTERING KEY
    * song varchar
    * itemInSession int
    * first_name varchar
    * last_name varchar

* songplay3:
    * song varchar PRIMARY KEY
    * first_name varchar
    * last_name varchar
    
## How to run
1. Run create_table.py (python3 create_table.py)
2. Run etl.py (python3 etl_pipeline.py)
3. Check data in database via running test.ipynb
