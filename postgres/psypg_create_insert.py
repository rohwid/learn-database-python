import os
from dotenv import load_dotenv
from libdags import helper

log_file="training_log.json"

column_name=["train_id", "project_id", "timestamp", "is_success", "train_duration", "train_metric", "err_message"]

timestamp="1234567890"

env_list = ['pacmann', 'pacmann123', '0.0.0.0', '30000', 'service_db']

helper.insert_log("tb_training_log", "ner", column_name, timestamp, log_file, env_list)