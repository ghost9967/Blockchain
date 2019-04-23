import uuid
import hashlib
import sqlite3
#v 1.0.2
m = range(10)
class BlockChain:
    '''This class is used to develop the blockchain architecture. It uses hashlib to generate hashes'''
    #This is the class description
    value = "$"
    hashi = "$"
    prevh = "$"
    #blockcahin class with previou hash , next hash and data
    def create(self):
        print("\n")
        print("------------------------Blockchain Voter System V 1.0.1-------------------------------")
        #print("------------------------Blockchain Voter System V 1.0.2-------------------------------")
        
        self.value = str(input("Enter your vote  "))
        self.hashi = hashlib.md5(self.value.encode())
        self.hashi = self.hashi.hexdigest()
        #creates the data block - encryted
    def insert(self,s):
        self.prevh = s
        #conn = sqlite3.connect('hash.db')
        #cursor = conn.execute("SELECT hash from HDB")
        #for i in cursor:
            #hash1 = i[0]
        #conn.close()
        #conn = sqlite3.conect('votes'+hash1+'.db')
        conn = sqlite3.connect('votes.db')
        #conn.execute('INSERT INTO votes'+hash1+' VALUES (?,?)',(self.hashi,self.prevh,))
        conn.execute("INSERT INTO votes VALUES (?,?)",(self.hashi,self.prevh,))
        #Attaches the block to the existing chain
        conn.commit()
        conn.close()
        print("Inserted")
i=0
prev="$"

while True:
    ob = BlockChain()
    ob.create()
    #Object named ob created and initialized
    print(ob.hashi)
    ob.insert(prev)
    prev = ob.hashi
    n=input("Continue? y/n  ")
    #Conditional Statement for iteration break
    if n =='n' or n=='N':
        break

