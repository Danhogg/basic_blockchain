from blockchain import BlockChain
# this file will be used to test the blockchain and see if it picks up tampering of blocks
# the proof of work in the blockchain can make the computer run hot and can take a lot of power
# so expect that if this code is tested. May be worth commenting out the proof of work method in 
# the blockchain file if your laptop is struggling


# this will create and print the contents of a blockchain with 2 blocks in it
transactions = [{'amount': '30', 'sender': 'Maxime', 'receiver': 'Dan'}, {'amount': '100', 'sender': 'Joel', 'receiver': 'Maxime'}]
new_blockchain = BlockChain()
new_blockchain.add_block(transactions)
new_blockchain.print_blockchain()

# here we will try and change the transactions of the second block with a subtle change in the first dictionary of the list
new_blockchain.chain[1].transactions = [{'amount': '130', 'sender': 'Maxime', 'receiver': 'Dan'}, {'amount': '100', 'sender': 'Joel', 'receiver': 'Maxime'}]

new_blockchain.validate_chain() # returns false and lets us know the blockchain has been altered



# we will use this transactions to test all of our other features in blockchain.py
one_transaction = {"amount":"50", "sender":"Alice", "receiver": "Bob"}
two_transaction = {"amount":"25", "sender": "Bob", "receiver":"Cole"}
three_transaction = {"amount":"35", "sender":"Alice", "receiver":"Cole"}

# check the genesis block is made automatically
our_blockchain = BlockChain()
our_blockchain.print_blockchain()

our_blockchain.add_block(one_transaction)
our_blockchain.add_block(two_transaction)
our_blockchain.add_block(three_transaction)
our_blockchain.print_blockchain()