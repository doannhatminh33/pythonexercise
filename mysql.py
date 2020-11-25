import csv
import MySQLdb

connection = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='customerdb')
cursor = connection.cursor()

CustomerTableSql="""CREATE TABLE Customers(customerid INT(20) PRIMARY KEY,
firstname CHAR(20) NOT NULL,lastname CHAR(20),companyname CHAR(20),
billingaddress1 CHAR(50),billingaddress2 CHAR(50),city CHAR(20),state CHAR(10),
postalcode CHAR(20),country CHAR(20),phonenumber CHAR(20),emailaddress CHAR(50),createddate DATETIME)"""
cursor.execute(CustomerTableSql)

csv_data = csv.reader(open('C:/Users/DELL/python/customer.csv'))
AddCustomerSql="INSERT INTO Customers(customerid,firstname,lastname,companyname,billingaddress1,billingaddress2,city,state,postalcode,country,phonenumber,emailaddress,createddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for row in csv_data:
    cursor.execute(AddCustomerSql,row)
connection.commit()
connection.close()