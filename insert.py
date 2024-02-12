import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'ALLAN KIMANI',18,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'MARK KURIA',32,145000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'TELVIN KAROGO',20,15000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'MAUREEN MUTHONI',33,45000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'LEON JAMES',40,55000.00)")

conn.commit()
print("RECORDS INSERTED SUCCESSFULLY")
conn.close()