from liblearn import helper

dir = '/home/rohwid/GitHub/learn-databases/postgres/files'
env_list = ['learn', 'learn123', '0.0.0.0', '5432', 'db_learn']
table_name = "tb_coba"

if __name__ == '__main__':
    helper.create_dataset_pandas(
        f"{dir}/entity_relation_dataset_large.tsv", 
        env_list, 
        table_name, 
        header=True, 
        delim='\t', 
        data_type='file'
    )

