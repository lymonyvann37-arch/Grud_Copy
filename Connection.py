import pymysql

def connectDB():
    return pymysql.connection(
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="crud_product"
    )

    #ត្រូវហៅ function មកប្រើប្រាស់ជាមុនសិន
conn = connectDB
if conn:
    print("connect to database sucessfully!")
else:
    print("connect to database failled!")