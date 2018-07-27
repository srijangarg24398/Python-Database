import pymysql.cursors

dsn_database = "test"
dsn_hostname = "localhost"
dsn_port = 3306
dsn_uid = "xxxxxx"
dsn_pwd = "xxxxxx" 

conn = pymysql.connect(host=dsn_hostname, port=dsn_port, user=dsn_uid, passwd=dsn_pwd, db=dsn_database)

# Create table
conn.query("""DROP TABLE IF EXISTS Cars""")
conn.query("""CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)""")

# Insert Data
conn.query("""INSERT INTO Cars VALUES(1,'Audi',52642)""")
conn.query("""INSERT INTO Cars VALUES(2,'Mercedes',57127)""")
conn.query("""INSERT INTO Cars VALUES(3,'Skoda',9000)""")
conn.query("""INSERT INTO Cars VALUES(4,'Volvo',29000)""")
conn.query("""INSERT INTO Cars VALUES(5,'Bentley',350000)""")
conn.query("""INSERT INTO Cars VALUES(6,'Citroen',21000)""")
conn.query("""INSERT INTO Cars VALUES(7,'Hummer',41400)""")
conn.query("""INSERT INTO Cars VALUES(8,'Volkswagen',21600)""")

# Create cursor to query data
cursor=conn.cursor()
cursor.execute("""SELECT * FROM Cars""")
print (cursor.fetchone())
print (cursor)

print ("\nShow me the cars:\n")
rows = cursor.fetchall()
import pprint
pprint.pprint(rows)

conn.close()
