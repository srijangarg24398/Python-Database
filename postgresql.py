import psycopg2
import sys

dsn_database = "testdb"
dsn_hostname = "localhost" 
dsn_port = "5432"         
dsn_uid = "xxxxxx"  
dsn_pwd = "xxxxxx"   
try:
    conn_string = "host="+dsn_hostname+" port="+dsn_port+" dbname="+dsn_database+" user="+dsn_uid+" password="+dsn_pwd
    print("Connecting to database\n	->%s" % (conn_string))
    conn=psycopg2.connect(conn_string)
    print("Connected!\n")
except:
    print("Unable to connect to the database.")

cursor = conn.cursor()
cursor.execute("""SELECT datname from pg_database""")
rows = cursor.fetchall()

print("\nShow me the databases:\n")
for row in rows:
    print ("   ", row[0])

# Create the table
cursor.execute("DROP TABLE IF EXISTS Cars")
cursor.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")

# Insert Data into table
cursor.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
cursor.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
cursor.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
cursor.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
cursor.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
cursor.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
cursor.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
cursor.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")

conn.commit()

cursor.execute("""SELECT * from Cars""")
rows = cursor.fetchall()

print("\nShow me the Cars:\n")
import pprint
pprint.pprint(rows)

for row in rows:
    print(" Number=", row[0] ,"  Name=", row[1],"  Price", row[2])

fout = open('cars.csv', 'w')
cursor.copy_to(fout,'cars',sep=",")

fin=open('cars.csv','r')
cursor.copy_from(fin,'cars',sep=",")

conn.commit()
conn.close()