import pandas as pd

#--------------------------------------------------- Funciones ------------------------------------------------------------#

def create_dataframe_sql(connection, data, data_name):
    dataframe = pd.DataFrame(data)
    try:
        dataframe.to_sql(data_name, connection, index=False, if_exists='replace')
        return print(f'Dataframe "{data_name}" creada exitosamente.')
    except Exception as e:
        print(F'Error creando la dataframe: {e}.')
        
# ----------------------------------------------------------------------------------------------------------------------- #

def excecute_query_tables(connection):
    query_tables = """
    SELECT table_name
    FROM INFORMATION_SCHEMA.TABLES
    WHERE table_catalog = 'postgres' AND table_schema = 'public'
    ORDER BY table_name
    """
    tables = pd.read_sql(query_tables, connection)['table_name'].tolist()
    return tables

# ----------------------------------------------------------------------------------------------------------------------- #

def create_df_variable(tables, connection):
    dataframes = {}
    for table_name in tables:
        query = f'SELECT * FROM {table_name}'
        dataframes[table_name] = pd.read_sql_query(query, connection)
    return dataframes

# ----------------------------------------------------------------------------------------------------------------------- #

def excecute_query(query, connection):
    result = pd.read_sql(query, connection)
    return result

# ----------------------------------------------------------------------------------------------------------------------- #