import os
import psycopg2
import pandas as pd

from liblearn import helper

t_host = "0.0.0.0"
t_port = "30000"
t_dbname = "service_db"
t_user = "pacmann"
t_pw = "pacmann123"

connection = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
cursor = connection.cursor()

request = f"SELECT * FROM tb_coba"

csv_table = f"COPY ({request}) TO STDOUT WITH CSV HEADER"

dir = '/home/rohwid/GitHub/learn-databases/postgres/files'
csv_file = f"{dir}/dump_tab_separated_data_large.csv"
out_file = f"{dir}/dump_tab_separated_data_large.tsv"

try:
    with open(csv_file, 'w') as f_output:
        cursor.copy_expert(csv_table, f_output)
        
    helper.clean_header_index(csv_file, header=True, delim=',')
    helper.csv_converter(csv_file, header=True, delim='\t', src_type='csv', dst_type='tsv')
    os.remove(csv_file)
    helper.compress_gzip(out_file)
    os.remove(out_file)
except psycopg2.Error as e:
    print(e)

cursor.close()
connection.close()

