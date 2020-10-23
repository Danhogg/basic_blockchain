from hashlib import sha256
# this file is for a general idea of nonce and PoW as to how it provides security
# also takes a good chunk of computing power
transactions = [{'amount': '30', 'sender': 'Maxime', 'receiver': 'Dan'}, {'amount': '100', 'sender': 'Joel', 'receiver': 'Maxime'}]

# this sets the required number of leading 0's that must be found in the hash produced by the nonce
difficulty = 2
# set the nonce to 0 and increment from there
nonce = 0

nonce_transactions = str(nonce) + str(transactions)
proof = sha256(nonce_transactions.encode()).hexdigest()

print(proof)

# here we find a proof that has 2 leading 0's
while (proof[:2] != '0' * difficulty):
    nonce += 1
    proof = sha256(nonce_transactions.encode()).hexdigest()

print(proof)