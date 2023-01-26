
# uvicorn api_python:app --reload

import pandas as pd
from fastapi import FastAPI
app = FastAPI()

from fastapi.responses import StreamingResponse # Add to Top


@app.get("/{Name}")
def get_csv_data(Name:str):
#     import pandas as pd
    import sqlite3
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()
    # load the data into a Pandas DataFrame
    data = pd.read_csv('Titanic Dataset.csv')
    # write the data to a sqlite table
    data.to_sql('data', conn, if_exists='append', index = False)



    # service_code=('21')

    # Type1=('per diem')
    #   query = "SELECT distinct u.billing_code, u.provider_group_id, o.NPI, u.Nogotiated_Price1 as Nogotiated_Price , o.TIN_TYPE, u.Billing_class1 as Billing_class, u.description FROM users u INNER JOIN orders o ON u.provider_group_id = o.provider_group_id where u.billing_code = '{}'".format(billing_code)
    Name='%'+Name+'%'
    # query = "SELECT distinct u.billing_code, u.provider_group_id, o.NPI, u.Nogotiated_Price1 as Nogotiated_Price , o.TIN_TYPE, u.Billing_class1 as Billing_class, u.description FROM users u INNER JOIN orders o ON u.provider_group_id = o.provider_group_id where u.description like '{}'".format(description)
    query = "SELECT distinct Name, PassengerId,Survived FROM data where Name like '{}'".format(Name)

    c.execute(query)
    a=c.fetchall()
    Name= [] 
    PassengerId=[]
    Survived=[]
#     Description=[]

    for i in range(len(a)):
    #     Billing_code.append(a[i][0])
        Name.append(a[i][0])
        PassengerId.append(a[i][1])
        Survived.append(a[i][2])
    
#     output={'Billing_code': Billing_code, 'Description': Description} 
    output={'Name': Name,'PassengerId':PassengerId,'Survived':Survived} 
    import json
    df=[]
    for i in range(len(a)):
        df.append({"Name": output['Name'][i],"PassengerId": output['PassengerId'][i],"Survived": output['Survived'][i]})


# convert into json
#     final = json.dumps(data, indent=2)
    return df
    


     
# dictionary of lists  
#     dict = {'Provider_group_id': Provider_group_id, 'Description': Description}  
#     return {'data':{'Billing_code': Billing_code, 'Description': Description} }
#     return {'Billing_code': Billing_code, 'Description': Description} 
#     df = pd.DataFrame(dict) 
#     return {'data':{"item_id_sachin": item_id, "My_name": name}}
    
# saving the dataframe 

#     return StreamingResponse(iter([df.to_csv(index=False)]),media_type="text/csv",headers={"Content-Disposition": f"attachment; filename=Provider_group_id_with_Description.csv"})






