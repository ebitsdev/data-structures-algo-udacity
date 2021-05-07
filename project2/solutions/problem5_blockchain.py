import datetime, hashlib

class Block:
    def __init__(self, data, prev_hash):
        self.timestamp = self.time_utility()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

    def time_utility(self):
        t_f = datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

        return t_f


class MyBlockChain:

    def __init__(self):
        self.head = None

    def chain_blocks(self, data):
        if not self.head:
            self.head = Block(data, 0)
        else:
            c_head = self.head
            
            while c_head.next:
                c_head = c_head.next
            prev_hash = c_head.hash
            c_head.next = Block(data, prev_hash)

    def show_block_details(self):
        if self == None:
            print("No block to show")
            return
        if self.head == None:
            print("No block to process")
            return
            
        else:
            c_head = self.head
            idx = 0
            print("======================================")
            print("Getting block details ...")

            while c_head:
                if c_head.data:
                    print("The block index is: {}".format(idx))
                    print("The block timestamp is: {}".format(c_head.timestamp))
                    print("The block data is: {}".format(c_head.data))
                    print("The block hash is: {}".format(c_head.hash))
                    print("The block previous hash is: {}".format(c_head.prev_hash))
                else:
                    print("The block has no data")

                # set the c_head to the next
                c_head = c_head.next

                idx += 1
            print("Done printing block details.")

myCoin = MyBlockChain()
# Test case 1
myCoin.chain_blocks("1st block data")
myCoin.chain_blocks("2nd block data")
myCoin.show_block_details()
# Test case 2
myCoin.chain_blocks("Another block data.")
myCoin.show_block_details()
# Test case 3 with empty string
myCoin.chain_blocks("")
myCoin.show_block_details()

# Test case 4 with empty block
myCoin2 = MyBlockChain()
myCoin2.show_block_details()

# Test case 5 block is None 
data3 = None
myCoin3 = MyBlockChain()
myCoin3.chain_blocks(data3)
myCoin3.show_block_details()






