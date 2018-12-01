#!/usr/bin/python3

# {
#     "index":0, // 块索引
#     "timestamp:"", // 时间戳
#     "transactions":{ // 交易信息，一个数组
#         "sender":"",  // 交易发送者
#         "recipient":"", // 交易接受者
#         "amount":"100.00" // 交易金额
#     },
#     "proof":"", // 工作量证明
#     "previous_hash":"" // 上一个区块的哈希值
# }
import hashlib
import json
import time
from flask import Flask, Response, jsonify, request


class Blockchain:
    def __init__(self):
        self.chain = []  # 链结构信息
        self.current_transactions = []  # 当前交易信息
        self.new_block(proof=100, previous_hash=1)

    # 新区块
    def new_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.last_block())
        }

        # 交易信息清空
        self.current_transactions = []
        self.chain.append(block)
        return block

    # 新交易
    def new_transaction(self, sender, recipient, amount)->int:
        self.current_transactions.append(
            {
                "sender": sender,
                "recipient": recipient,
                "amount": amount
            }
        )
        return self.last_block("index") + 1

    # 静态Hash
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_string).hexdigest()

    # 最后一个区块
    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof: int)->int:
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def valid_proof(self, last_proof: int, proof: int)->bool:
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        # time.sleep(1)
        # print(guess_hash)
        return guess_hash[0:4] == "0000"


# newPow = Blockchain()
# newPow.proof_of_work(100)

app = Flask(__name__)
blockchacin = Blockchain()
# 产生交易 http://127.0.0.1:5000/transactions/new


@app.route('/transactions/new', methods=['POST'])
def new_transactions():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']

    if values is None:
        return "Values is Null", 400
    if not all(k in values for k in required):
        return "Missind values", 400
    index = blockchacin.new_transaction(
        values['sender'], values['recipient'], values['amount'])

    response = {"message": f'Transactions will be added to Block {index}'}
    return jsonify(response), 201

# 挖矿


@app.route('/mine', methods=['GET'])
def mine():
    return "This Will A New Mine"

# 返回所有的区块链


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchacin.chain,
        'length': len(blockchacin.chain)
    }
    # flask提供了jsonify函数供用户处理返回的序列化json数据
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
