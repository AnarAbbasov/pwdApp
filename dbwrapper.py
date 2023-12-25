import pyodbc

SERVER = '192.168.1.106'
DATABASE = 'ProductionDB'
USERNAME = 'sa'
PASSWORD = ''

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}; Encrypt=no'

conn = pyodbc.connect(connectionString) 

SQL_QUERY ="""Select name from TestTable"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f'Name {r}')
