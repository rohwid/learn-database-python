from liblearn import helper

dir = '/home/rohwid/GitHub/learn-databases/postgres/files'

env_list = ['pacmann', 'pacmann123', '0.0.0.0', '30000', 'service_db']

table_name = "tb_coba"

helper.create_dataset_pandas(f"{dir}/data_input_large.tsv", env_list, table_name, header=True, delim='\t')

