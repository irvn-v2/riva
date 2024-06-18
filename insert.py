import sqlite3

conn = sqlite3.connect('test.db')
print("Successfully connected")

conn.execute("INSERT INTO TEACHER VALUES(1,'James', 'Kariuki', 45, 56000.00)")
conn.execute("INSERT INTO TEACHER VALUES(2,'Nicole', 'Wambui', 17, 45000.00)")
conn.execute("INSERT INTO TEACHER VALUES(3,'Caleb', 'Kimutai', 18, 67000.00)")
conn.execute("INSERT INTO TEACHER VALUES(4,'Yna', 'Brown', 17, 36000.00)")
conn.execute("INSERT INTO TEACHER VALUES(5,'Joel', 'Odhiambo', 19, 49000.00)")
conn.execute("INSERT INTO TEACHER VALUES(6,'Tamasha', 'Mawia', 18, 72000.00)")

conn.commit()
print("Successfully inserted records")

conn.close()