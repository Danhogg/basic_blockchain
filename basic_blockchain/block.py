from datetime import datetime
from  hashlib import sha256
# creating a class of block for making new blocks in the blockchain
class Block:
    #default constructor for block
    def __init__(self, transactoins, previous_hash, nonce = 0):
        self.transactions = transactoins
        self.previous_hash = previous_hash
        self.nonce = nonce 
        self.timestamp = datetime.now()
        self.hash = self.generate_hash()

    def print_content(self):
        # this will print the contents of a block
        print('timestamp:', self.timestamp)
        print('transactions', self.transactions)
        print('previous_hash', self.previous_hash)

    def generate_hash(self):
        # creates the hash for the block from the contents
        block_content = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
        block_hash = sha256(block_content.encode())
        return block_hash.hexdigest()