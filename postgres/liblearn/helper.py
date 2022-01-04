import time
import json
import pandas as pd
import gzip
import shutil

from sqlalchemy import create_engine


def generate_file_timestamp(name):
    current_time = time.time()
    time_obj = time.localtime(current_time)
    
    for_id = "%d%d%d%d%d%d" % (
        time_obj.tm_year,
        time_obj.tm_mon,
        time_obj.tm_mday,
        time_obj.tm_hour, 
        time_obj.tm_min, 
        time_obj.tm_sec
    )
    
    return f"{name}-{for_id}"


def generate_date_timestamp():
    current_time = time.time()
    time_obj = time.localtime(current_time)
    
    for_date = "%d%d%d%d%d%d" % (
        time_obj.tm_year,
        time_obj.tm_mon,
        time_obj.tm_mday,
        time_obj.tm_hour, 
        time_obj.tm_min, 
        time_obj.tm_sec
    )

    return f"{for_date}"


def compress_gzip(file_path):
    with open(file_path, 'rb') as f_in:
        file_path = file_path[:len(file_path) - 4]
        
        with gzip.open(f"{file_path}.gz", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def get_json_value(log_file):
    with open(log_file) as json_file:
        params = json.load(json_file)
        params['training_duration'] = float(params['training_duration'].split()[0])
        params['training_metric'] = json.dumps(params['training_metric'])
        
        val_list = []
        
        for param in params:
            val_list.append(params[param])
            
        return val_list

""" 
set_dataset_header(
    file_path,      # stirng: '/home/rohwid/GitHub/learn-databases/files/tab_separated_data_large.tsv'
    column_names,   # list: [column1, column2] (optional)
    header=None,    # bolean: True/False
    delim=None      # sting: 'whitespace', '\n', and '\t'
) 
"""
def set_dataset_header(*args, **kwargs):
    if kwargs['header'] == False or kwargs['header'] == None:
        if kwargs['delim'] == 'whitespace' or kwargs['delim'] == None:
            df = pd.read_csv(args[0], header=None, delim_whitespace=True)
        elif kwargs['delim'] == '\n':
            df = pd.read_csv(args[0], header=None, sep='\n')
        elif kwargs['delim'] == '\t':
            df = pd.read_csv(args[0], header=None, sep='\t')
        elif kwargs['delim'] == ',':
            df = pd.read_csv(args[0], sep=',')
        else:
            print('[ERROR] Delimiter option unknown.')
            quit()
        
        if len(args) == 2:
            df.columns = args[3]

    elif(kwargs['header'] == True):
        if kwargs['delim'] == 'whitespace' or kwargs['delim'] == None:
            df = pd.read_csv(args[0], delim_whitespace=True)
        elif kwargs['delim'] == '\n':
            df = pd.read_csv(args[0], sep='\n')
        elif kwargs['delim'] == '\t':
            df = pd.read_csv(args[0], sep=r'\t', encoding='utf-8')
        elif kwargs['delim'] == ',':
            df = pd.read_csv(args[0], sep=',')
        else:
            print('[ERROR] Delimiter option unknown.')
            quit()
    else:
        print('[ERROR] Header option unknown.')
        quit()

    return df


""" 
csv_converter(
    file_path,          # stirng: '/home/rohwid/GitHub/learn-databases/files/tab_separated_data_large.tsv'
    column_names,       # list: [column1, column2] (optional)
    header=None,        # bolean: True/False
    delim=None,         # string: 'whitespace', '\n', and '\t'
    dst_type=None       # string: 'csv', 'tsv', 'txt', and etc
)
"""
def csv_converter(*args, **kwargs):
    if kwargs['header'] == False or kwargs['header'] == None:
        df = set_dataset_header(*args, header=kwargs['header'], delim=',')
    elif(kwargs['header'] == True):
        df = set_dataset_header(*args, header=kwargs['header'], delim=',')
    else:
        print('[ERROR] Header option unknown.')
        quit()
    
    file_path = args[0][:len(args[0]) - 4]

    if kwargs['header'] == True:
        df.to_csv(f"{file_path}.{kwargs['dst_type']}", index=None, sep=kwargs['delim'])
    else:
        df.to_csv(f"{file_path}.{kwargs['dst_type']}", index=None, header=None, sep=kwargs['delim'])


""" 
clean_header_index(
    file_path,          # stirng: '/home/rohwid/GitHub/learn-databases/files/tab_separated_data_large.tsv'
    column_names,       # list: [column1, column2] (optional)
    header=None,        # bolean: True/False
    delim=None,         # string: 'whitespace', '\n', and '\t'
)
"""
def clean_header_index(file_path, **kwargs):
    if kwargs['header'] == True:
        df = set_dataset_header(file_path, **kwargs)
        df = df.iloc[:, 1:]
        df.to_csv(file_path, index=None, sep=kwargs['delim'])
    elif kwargs['header'] == False:
        df = set_dataset_header(file_path, **kwargs)
        df = df.iloc[1:, 1:]
        df.to_csv(file_path, index=None, header=None, sep=kwargs['delim'])
    else:
        print("[ERROR] Invalid header value.")


""" 
create_dataset_pandas(
    file_path,      # stirng: '/home/rohwid/GitHub/learn-databases/files/tab_separated_data_large.tsv'.
    env_list,       # list: ['pacmann', 'pacmann123', '0.0.0.0', '30000', 'service_db'].
    table_name,     # string: 'tb_service'.
    columns_name,   # list or string: column1 or[column1, column2] (optional).
    header=None,    # bolean: True/False.
    delim=None      # string: 'whitespace', '\n', or '\t'.
    data_type=None  # string: 'dataframe' or 'file'.
) 
"""
def create_dataset_pandas(*args, **kwargs):
    env_list = args[1]
    table_name = args[2]

    if kwargs['data_type'] == 'file':
        if kwargs['header'] == False or kwargs['header'] == None:
            df = set_dataset_header(args[0], args[3], **kwargs)
        elif(kwargs['header'] == True):
            df = set_dataset_header(args[0], **kwargs)
        else:
            print('[ERROR] Header option unknown.')
            quit()
    elif kwargs['data_type'] == 'dataframe':
        df = args[0]
    else:
        print('[ERROR] Data type unknown.')
        quit()

    engine = create_engine(
        f"postgresql+psycopg2://{env_list[0]}:{env_list[1]}@{env_list[2]}:{env_list[3]}/{env_list[4]}",  
        pool_recycle=3600
    )

    connection = engine.connect()

    try:
        df.to_sql(table_name, connection, if_exists='replace', index=True, chunksize=2000)
    except ValueError as val_err:
        print(val_err)
    except Exception as err:
        print(err)
    else:
        print(f"PostgreSQL Table {table_name} has been created successfully.")
    finally:
        connection.close()


###########################################
# Custom Dataset Handler for NER
###########################################

def encode_unicode(sentence):
    return sentence.encode('unicode_escape').decode('utf-8')


def decode_unicode(sentence):
    return sentence.encode().decode('unicode-escape')


def convert_ner_dataset(dataset, columns_name):
    lines = open(dataset).readlines()
    res_file = []
    res_sentence = ''
    for line in lines:
        if line.strip() != '':
            ln = '\t'.join(line.strip().split()) + '\n'
            res_sentence += ln
        elif line.strip() == '' and res_sentence == '':
            continue
        elif line.strip() == '':
            res_file.append(encode_unicode(res_sentence) + '\n')
            res_sentence = ''
    res_file.append(encode_unicode(res_sentence))

    return pd.DataFrame(res_file, columns=[columns_name])


def dump_ner_dataset(dataset, env_list, table_name, columns_name):
    engine = create_engine(
        f"postgresql+psycopg2://{env_list[0]}:{env_list[1]}@{env_list[2]}:{env_list[3]}/{env_list[4]}",  
        pool_recycle=3600
    )

    connection = engine.connect()

    df = pd.read_sql(f"SELECT {columns_name} FROM {table_name} order by index", connection)
    sentences = df[columns_name].apply(lambda x: x.encode().decode('unicode-escape').strip()).values
    sentences = '\n\n'.join(sentences)
    open(dataset, 'w+').write(sentences)

