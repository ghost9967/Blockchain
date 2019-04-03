import sqlite3

conn = sqlite3.connect('votes.db')
cursor = conn.execute("SELECT hash from votes")
for row in cursor:
   print ("Hash = ", row[0])

conn.close()
   
