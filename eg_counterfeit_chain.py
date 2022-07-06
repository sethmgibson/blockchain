from Blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender': 'Alice', 'receiver': 'Bob'},
                    {'amount': '55', 'sender': 'Bob', 'receiver': 'Alice'}]

my_blockchain = Blockchain()
my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()
my_blockchain.valid_chain

my_blockchain.chain[1].transactions = 'Fake Transaction'
my_blockchain.print_blocks()
my_blockchain.valid_chain

