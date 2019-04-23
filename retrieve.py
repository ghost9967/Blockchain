import sqlite3
#v 1.0.2
#conn = sqlite3.connect('hash.db')
#hash1 = conn.execute("SELECT hash from HDB")
#for i in hash1:
   #nh = i[0]
#conn.close()
#conn = sqlite3.connect('votes'+nh+'.db')
conn = sqlite3.connect('votes.db')
cursor = conn.execute("SELECT hash,prev from votes")
print("------------------------------------Blockchain Voting System v1.0.1------------------------------------------")
#print("------------------------------------Blockchain Voting System v1.0.2------------------------------------------")
for row in cursor:
   print ("Hash = ", row[0])
   print ("Previous Hash = ", row[1])
   print ("\n")
conn.close()
   
