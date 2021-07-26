import pandas as pd

from sqlalchemy import create_engine
from liblearn import helper

dir = '/home/rohwid/GitHub/learn-databases/postgres/files'
env_list = ['pacmann', 'pacmann123', '0.0.0.0', '30000', 'service_db']
table_name = "tb_coba"

#e = create_engine('postgresql+psycopg2://postgres:kucing@127.0.0.1/postgres')
#con = e.conn

""" 
def dump_ner_data_from_db(outfile):
    df = pd.read_sql("select kalimat from ner order by index", con)
    kalimats = df['kalimat'].apply(
        lambda x: x.encode().decode('unicode-escape').strip()
    ).values
    kalimats = '\n\n'.join(kalimats)
    open(outfile, 'w+').write(kalimats)


def dump():
    training_data = 'ner-dataset.txt'
    dump_ner_data_from_db(training_data)
"""

if __name__ == '__main__':
    input_dataset = f"{dir}/ner_dataset_large.txt"
    df = helper.convert_ner_input_to_db(input_dataset)
    helper.create_dataset_pandas(df, env_list, table_name, data_type='dataframe')