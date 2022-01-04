from liblearn import helper

dir = '/home/rohwid/GitHub/learn-database-python/postgres/files/4w_ranker_dataset'
env_list = ['learn', 'learn123', '0.0.0.0', '5440', 'db_learn']
table_name = "tb_4w_ranker_dataset"

if __name__ == '__main__':
    helper.create_dataset_pandas(
        f"{dir}/4w_23nov.tsv", 
        env_list, 
        table_name, 
        header=True, 
        delim='\t', 
        data_type='file'
    )

