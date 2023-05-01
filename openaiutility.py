import openai
def create_table_definition_prompt(df,table_name):
    prompt="""sqllite with properties {}({}) #""".format(table_name,','.join(str(x) for x in df.columns))
    return prompt

#def user_query(x):
    user_input=x
    return user_input


def combine_prompt(fixed_sql_prompt,user_query):
    final_user_input=f'##a query to answer:{user_query}\nSELECT'
    return fixed_sql_prompt+final_user_input

def send_to_openai(prompt):
    response=openai.Completion.create(
        engine='text-davinci-003',prompt=prompt,temperature=0,max_tokens=150,stop=['#',';'])
    return response