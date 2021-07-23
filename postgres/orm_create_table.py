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


env_user = "pacmann"
env_password = "pacmann123"
env_address = "0.0.0.0"
env_port = 30000
env_db = "service_db"

engine = create_engine(
    f"postgresql+psycopg2://{env_user}:{env_password}@{env_address}:{env_port}/{env_db}", 
    pool_recycle=3600
)

meta = MetaData()

training_log = Table(
    'tb_training_log', meta, 
    Column('train_id', INTEGER, primary_key = True), 
    Column('project_id', VARCHAR), 
    Column('timestamp', INTEGER),
    Column('is_success', BOOLEAN),
    Column('train_duration', FLOAT),
    Column('train_metric', JSON),
    Column('err_message', TEXT)
)

meta.create_all(engine)