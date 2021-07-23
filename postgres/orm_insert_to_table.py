import os
from dotenv import load_dotenv

import psycopg2
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.dialects.postgresql import \
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, \
    INTERVAL, JSON, JSONB, MACADDR, MONEY, NUMERIC, OID, REAL, SMALLINT, TEXT, \
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, \
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR

import json


env_user = "pacmann"
env_password = "pacmann123"
env_address = "0.0.0.0"
env_port = 30000
env_db = "service_db"


def insert_log(table_name, project, colums_name, timestamp, log_file, env_list):
    engine = create_engine(
        f"postgresql+psycopg2://{env_list[0]}:{env_list[1]}@{env_list[2]}:{env_list[3]}/{env_list[4]}", 
        pool_recycle=3600
    )
    
    with open(log_file) as json_file:
        param = json.load(json_file)
        param['training_duration'] = float(param['training_duration'].split()[0])
        
        param_list = list(param.keys())
        

        print("param1:", param[param_list[0]])
        print("param2:", param[param_list[1]])
        print("param3:", param[param_list[2]])
        print("param4:", param[param_list[3]])

    meta = MetaData()

    train_log = Table(
        table_name, meta, 
        Column(colums_name[0], INTEGER, primary_key = True), 
        Column(colums_name[1], VARCHAR), 
        Column(colums_name[2], INTEGER),
        Column(colums_name[3], BOOLEAN),
        Column(colums_name[4], FLOAT),
        Column(colums_name[5], JSON),
        Column(colums_name[6], TEXT)
    )

    conn = engine.connect()
    conn.execute(train_log.insert().values(
            project_id = project, 
            timestamp = timestamp,
            is_success = param[param_list[0]],
            train_duration = param[param_list[1]],
            train_metric = param[param_list[2]],
            err_message = param[param_list[3]]
        )
    )