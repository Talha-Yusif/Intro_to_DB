import mysql.connector
from mysql.connector import Error


try:
    connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Physics3939$'
    
    
    )
    create_database="""
    CREATE DATABASE IF NOT EXISTS alx_book_store
    """
    

    cursor=connection.cursor()
    cursor.execute(create_database)
    print(" Database 'alx_book_store' created successfully!")
    cursor.close()
   
except mysql.connector.Error as e :
    print(e)
finally:
    if connection.is_connected():
        connection.close()
