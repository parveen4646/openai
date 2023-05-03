from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
def dataframe_to_database(df,table_name):
    """conver a pandas dataframe toa database"""
    engine=create_engine(f'sqlite:///:memory:',echo=True)
    df.to_sql(name=table_name,con=engine,index=False)
    return engine
def handle_response(response):
    query=response['choices'][0]['text']
    if query.startswith(' '):
        query='SELECT' + query
    return query
def excecute_query(engine,query):
    with engine.connect() as conn:
        result=conn.execute(text(query))
        result=pd.DataFrame(result.fetchall())
        return result