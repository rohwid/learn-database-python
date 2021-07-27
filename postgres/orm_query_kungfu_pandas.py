from liblearn import helper

dir = '/home/rohwid/GitHub/learn-databases/postgres/files'
env_list = ['pacmann', 'pacmann123', '0.0.0.0', '30000', 'service_db']
column_name = 'sentence'
table_name = "tb_coba"

if __name__ == '__main__':
    input_dataset = f"{dir}/input_ner_dataset_large.txt"
    df = helper.convert_ner_dataset(input_dataset, column_name)
    helper.create_dataset_pandas(df, env_list, table_name, data_type='dataframe')