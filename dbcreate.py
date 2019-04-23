import sqlite3
import hashlib
#v 1.0.2
#string = "WOW"
#hname = hashlib.md5(string.encode())
#hname = hname.hexdigest()\\
#print(hname)
#conn = sqlite3.connect('hash.db')
#conn.execute('''CREATE TABLE HDB (NAME VARCHAR(30) );''')
#conn.execute("INSERT INTO HDB VALUES (?)"),(hname,))
#conn.close
conn = sqlite3.connect('votes.db')
#conn = sqlite3.connect('votes'+hname+'.db')
#creates the database named votes.db
print("Connection Establised")
conn.execute('''CREATE TABLE VOTES
         (
         HASH   VARCHAR(30)    NOT NULL, PREV VARCHAR(30) );''')
#Table named votes created in localhost
print("Script executed successfully")
conn.commit()
#changes saved
conn.close()
