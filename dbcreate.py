import sqlite3
conn = sqlite3.connect('votes.db')
print("Connection Establised")
conn.execute('''CREATE TABLE VOTES
         (
         HASH   VARCHAR(30)    NOT NULL, PREV VARCHAR(30) );''')
print("Script executed successfully")
conn.commit()
conn.close()
