import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    # Manually create the first block (genesis block)
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash_value = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash_value)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add blocks to the blockchain
num_blocks_to_add = 5
for i in range(1, num_blocks_to_add + 1):
    new_data = f"Block #{i} Data"
    new_block = create_new_block(previous_block, new_data)
    blockchain.append(new_block)
    previous_block = new_block
    print(f"Block #{i} has been added to the blockchain!")
    print(f"Hash: {new_block.hash}\n")

# Validate the blockchain
def is_valid_chain(chain):
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i - 1]

        # Check if the previous hash matches
        if current_block.previous_hash != previous_block.hash:
            return False

        # Check if the hash is correct
        if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
            return False

    return True

# Validate and print the result
if is_valid_chain(blockchain):
    print("Blockchain is valid!")
else:
    print("Blockchain is not valid!")



