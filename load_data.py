import getpass
import snowflake.connector
import pandas as pd

df=pd.read_csv("WebTrackingData.csv")
#data=[]
splited_urls=[]
for i in df[df['CookieID']==444347088453210476]['RequestedURL'].str.split("/"):
    data=[j for j in i if j]
    #print(len(data)==7)
    if len(data)==3:
        data.extend(["","","",""])
    if len(data)==4:
        data.extend(["","",""])
    if len(data)==5:
        data.extend(["",""])
    if len(data)==6:
        data.extend([""])
        
    splited_urls.append(data)
df=pd.DataFrame(splited_urls)

#Getting user imputs to establish connection to snowflake

USER = input("PLEASE ENTER YOUR SNOWFLAKE USERNAME ")
PASSWORD = getpass.getpass("ENTER YOUR SNOWFLAKE PASSWORD ")


ACCOUNT = input("PLEASE ENTER YOUR SNOWFLAKE ACCOUNT NAME ")


#create snowflake database connection
conn= snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse='COHORT_XL',
    database = 'IMV_IMMUNOVACCINE_INC_DLBCL_RITUXIMAB_ANY_ANTHRACYCLINE',
    schema = 'SANDBOX'
)

cur=conn.cursor()

#Checking the conenction
cur

import pandas as p



write_pandas(conn, def, 'test')
