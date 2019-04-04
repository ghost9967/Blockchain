import sqlite3

conn = sqlite3.connect('votes.db')
cursor = conn.execute("SELECT hash,prev from votes")
for row in cursor:
   print ("Hash = ", row[0])
   print ("Previous Hash = ", row[1])
   print ("\n")

conn.close()
   
