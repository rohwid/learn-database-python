from liblearn import helper

dir = '/home/rohwid/GitHub/learn-databases/postgres/files'
env_list = ['pacmann', 'pacmann123', '0.0.0.0', '30000', 'service_db']
table_name = "tb_coba"
column_names = 'sentence'

if __name__ == '__main__':
    output_dataset = f"{dir}/output_ner_dataset_large.txt"
    helper.dump_ner_dataset(output_dataset, env_list, table_name, column_names)