#firs, we need to install mysql-connector-python in pycharm via settings.

import mysql.connector          #need to import mysql.connector module



insert_query="insert into Students values (1851,'Nagarajan','Vijayan', 345,'Chennai')"
update_query="update Students set StudentID=1856 where FirstName='Rajesh'"
delete="delete from Students where StudentID=1856"


#insert, update, delete
con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="studentDB")      #establish connection with MySQL database

cursor=con.cursor()             #establish cursor() function and saved in one variable to use furthur
cursor.execute("delete from Students where StudentID=1856")        #And execute our SQL query using that cursor() function
con.commit()            #And commit the transaction then only we saved those SQL query into our database otherwise it wont saved in database
con.close()                 #And finally we need to close the database connection.

print("Finished!!!!!!!!!!!!")