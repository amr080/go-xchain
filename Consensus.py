import hashlib
import time
import random

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", hashlib.sha256("Genesis Block".encode()).hexdigest())

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), previous_block.hash, int(time.time()), data, self.calculate_hash(len(self.chain), previous_block.hash, int(time.time()), data))
        self.chain.append(new_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = str(index) + previous_hash + str(timestamp) + data
        return hashlib.sha256(value.encode()).hexdigest()

blockchain = Blockchain()
