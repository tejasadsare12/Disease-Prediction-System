import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test",
    port="33060"
    )

cursor = con.cursor()
cursor.execute("SELECT * FROM TEST_TABLE")
data = cursor.fetchall()
name = cursor.column_names[1]
for row in data:
    for values in row:
        if(values == "tushar"):
            print(row)
            print(type(row))