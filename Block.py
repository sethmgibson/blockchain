from datetime import datetime as dt
from hashlib import sha256


class Block:
    def __init__(self, transactions, previous_hash, nonce=0):
        self.timestamp = dt.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def print_block(self):
        # Prints block contents
        # Returns void
        print("timestamp:", self.timestamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)

    def generate_hash(self):
        # Hash contents automatically generated upon instantiation
        # Returns hash
        contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(contents.encode())
        return block_hash.hexdigest()
