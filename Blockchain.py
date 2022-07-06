from Block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        # Automatically generates first block in chain
        # Returns chain list with genesis block added
        genesis_block = Block({}, "0")
        self.chain.append(genesis_block)
        return self.chain

    def print_blocks(self):
        # Prints blockchain contents
        # Returns void
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_block()

    def add_block(self, transactions):
        # Adds block to chain
        # Returns the added block with hash proof
        previous_hash = self.chain[len(self.chain) - 1].hash
        new_block = Block(transactions, previous_hash)
        proof = proof_of_work(new_block)
        self.chain.append(new_block)
        return proof, new_block

    @property
    def valid_chain(self):
        # True for valid chain, False for invalid
        # Returns bool
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print("The current hash of the block does not equal the generated hash of the block.")
                return False
            if current.previous_hash != previous.generate_hash():
                print("The previous block's hash does not equal the previous hash value stored in the current block.")
                return False
        print("The chain is valid.")
        return True


def proof_of_work(block, difficulty=2):
    # difficulty sets the number of leading zeros the nonce produces that must be found in the hash
    # Returns hash proof
    proof = block.generate_hash()
    while proof[:difficulty] != difficulty * '0':
        block.nonce += 1
        proof = block.generate_hash()
    block.nonce = 0
    return proof
