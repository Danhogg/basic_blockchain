from block import Block

class BlockChain:
    def __init__(self):
        self.chain = [] # an empty list that will contain every block
        self.all_transaction = []
        self.genesis_block()

    def genesis_block(self):
        # this creates the first block of the chain and sets its hash to 0 with
        # an empty transactions dictionary
        transactions = {}
        self.chain.append(Block(transactions, '0'))

    # allows us to add blocks to the block chain
    def add_block(self, transactions):
        # this grabs the hash of the block before the new one to be put in
        previous_block_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(transactions, previous_block_hash)
        final_proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return final_proof, new_block
        

    def validate_chain(self):
        # used to validate the blockchain and check for any attempted changes to blocks within
        for i in range (1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            # checks the current hash against what the current hash should be if generated
            # both if statements return False if the condition is met so we know if there
            # has been tampering 
            if (current.hash != current.generate_hash()):
                print("The hash of the block does not equal the generated hash for the block. A block has been changed")
                return False
            #checks hash of previous block against the previous hash value in the current block
            if (current.previous_hash != previous.generate_hash()):
                print("The previous block hash does not equal the previous hash value in the current block. A block has been changed")
                return False
            return True

    def proof_of_work(self, block, difficulty = 2):
        # implementing nonce and proof of work concepts
        proof = block.generate_hash()
        # this is a generalised while loop with difficulty set to 2 as default
        while proof[:difficulty] != '0' * difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        # set the nonce back to 0 for when this is used on the next block
        block.nonce = 0
        return proof

    # this will print all the block information for all blocks in the blockchain
    def print_blockchain(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print(f"Block {i} {current_block}")
            current_block.print_content()