import mysql.connector as connector
db = connector.connect(host="localhost",user="root",passwd="root",database="python")

mycursor = db.cursor()

# mycursor.execute("select * from products limit 34")
#
#
# results=mycursor.fetchall()
#
# for product in results:
#     print(product[1])
sql = "INSERT INTO products (name, quantity) VALUES (%s, %s)"
val = ("Tissue", "21")
mycursor.execute(sql, val)

db.commit()

print(mycursor.rowcount, "record inserted.")