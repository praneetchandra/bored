import os
import sqlalchemy
import psycopg2
import pandas as pd
import numpy as np
import datetime

#Establish Connection to Redshift Database for this tenant
engine = sqlalchemy.create_engine("postgresql://{}:{}@{}:{}/{}".format(os.environ['REDSHIFT_USERNAME'],
                                                                       os.environ['REDSHIFT_PASSWORD'],
                                                                       os.environ['REDSHIFT_HOST'],
                                                                       os.environ['REDSHIFT_PORT'],
                                                                       os.environ['TENANT']))

connection = engine.connect()
metadata = sqlalchemy.MetaData()
query = sqlalchemy.select([stage.ordersexport])
df = pd.DataFrame(query)
print(df)
