import uuid
import hashlib
import sqlite3


class BlockChain:
    '''This class is used to develop the blockchain architecture. It uses hashlib to generate hashes'''
    value = "$"
    hashi = "$"
    prevh = "$"
    def create(self):
        self.value = str(input("Enter your vote  "))
        self.hashi = hashlib.md5(self.value.encode())
        self.hashi = self.hashi.hexdigest()
    def insert(self,s):
        self.prevh = s
        conn = sqlite3.connect('votes.db')
        conn.execute("INSERT INTO votes VALUES (?,?)",(self.hashi,self.prevh,))
        conn.commit()
        conn.close()
        print("Inserted")
i=0
prev="$"

while True:
    ob = BlockChain()
    ob.create()
    print(ob.hashi)
    ob.insert(prev)
    prev = ob.hashi
    n=input("Continue? y/n  ")
    if n =='n':
        break

