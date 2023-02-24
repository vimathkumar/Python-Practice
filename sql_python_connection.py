# importing mysql connector
# connecting database with connector
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="kiran123"
)
# print(mydb)







# creating the Databases
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE d2022")


# # checking all the databases
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)








# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="kiran123",
#   database="d2022",
# )
# mycursor = mydb.cursor()





# creating table in databases
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# # show tables
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)




# #insert in SQL
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)



# mydb.commit()
# print(mycursor.rowcount, "record inserted.")






# # select in MySQl
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)









# # Where in Mysql
# sql = "SELECT * FROM customers WHERE address ='Highway 21'"
# mycursor.execute(sql)

# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)




# # delete in Mysql
# sql = "DELETE FROM customers WHERE address = 'Highway 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")






# # Drop
# mycursor = mydb.cursor()
# sql = "DROP TABLE customers"
# mycursor.execute(sql)



# # select in MySQl
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# # update table
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Highway 22'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")



# # Truncate
# mycursor = mydb.cursor()
# sql = "TRUNCATE TABLE customers"
# mycursor.execute(sql)



# # select in MySQl
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)