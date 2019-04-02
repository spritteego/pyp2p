import hashlib
import uuid

class Block(object):
    def __init__(self,data,previous_hash=None):
        self.identifier=uuid.uuid4().hex
        self.nonce=None
        self.data=data
        self.previous_hash=previous_hash
    def hash(self): #hash the block
        msg=hashlib.sha256()
        msg.update(self.identifier.encode('utf-8'))
        msg.update(str(self.nonce).encode('utf-8'))
        msg.update(str(self.data).encode('utf-8'))
        msg.update(str(self.previous_hash).encode('utf-8'))
        return msg.hexdigest()
    def hash_is_valid(self,next_hash):
        return next_hash[0:4]=="0000"
    def mine(self):
        cur_nonce=self.nonce or 0
        #loop to find correct nonce
        while 1:
            tmp=self.nonce
            self.nonce = cur_nonce
            next_hash=self.hash()

            if self.hash_is_valid(next_hash):
                # self.__setattr__(self,'nonce',cur_nonce)
                # self.nonce=cur_nonce
                break
            else:
                print(next_hash, self.nonce)
                self.nonce=tmp
                cur_nonce+=1


    def __repr__(self):
        return 'Block<Hash: {}, Nonce: {}>'.format(self.hash(), self.nonce)
# class Block
block=Block('hello world','0000000')

block.mine()
print(repr(block))
