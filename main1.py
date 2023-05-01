import os
import logging
import pandas as pd
import openai
import db_utility
import openaiutility

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)
openai.api_key='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'

if __name__ == '__main__':
    logging.info('Loading data..')
    df=pd.read_csv('car_sales.csv')
    logging.info(f'data_format: {df.shape}')

    logging.info('converting to database')
    database=db_utility.dataframe_to_database(df,'car_sales')

    fixed_sql_prompt=openaiutility.create_table_definition_prompt(df,'car_sales')
    logging.info(f'fixed_sql_prompt:{fixed_sql_prompt}')

    logging.info('waiting for input')
    user_input=openaiutility.user_query()
    final_prompt=openaiutility.combine_prompt(fixed_sql_prompt,user_input)
    logging.info(f'final promt{final_prompt}')

    logging.info('sending to openai')
    response=openaiutility.send_to_openai(final_prompt)
    proposed_query=response['choices'][0]['text']
    proposed_query_postprocessed=db_utility.handle_response(response)
    result=db_utility.excecute_query(database,proposed_query_postprocessed)
    logging.info(f'result{result}')
    print(result)
