import pandas as pd

#--------------------------------------------------- Funciones ------------------------------------------------------------#

def create_dataframe_sql(connection, data, data_name):
    dataframe = pd.DataFrame(data)
    try:
        dataframe.to_sql(data_name,connection, index=False, if_exists='replace')
        return print(f'Dataframe "{data_name}" creada exitosamente.')
    except Exception as e:
        print(F'Error creando la dataframe: {e}.')
        
# ----------------------------------------------------------------------------------------------------------------------- #
# Modificar esta función
def excecute_query_tables(connection):
    query_tables = """
    SELECT name 
    FROM sqlite_master 
    WHERE type = 'table'
    """
    result = pd.read_sql(query_tables,connection)['name'].tolist()
    return result

# ----------------------------------------------------------------------------------------------------------------------- #
# Modificar esta función
def create_df_variable(tables, connection):
    dataframes = {}
    for table_name in tables:
        query = f'SELECT * FROM {table_name}'
        dataframes[table_name] = pd.read_sql_query(query, connection)
    return dataframes

# ----------------------------------------------------------------------------------------------------------------------- #
# Modificar esta función
def excecute_query(query, connection):
    result = pd.read_sql(query, connection)
    return print(result)

# ----------------------------------------------------------------------------------------------------------------------- #