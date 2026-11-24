import csv

def read_data():
    transactions = []

    with open ("data/transactions.csv", "r", newline="") as file:
        csv_reader = csv.DictReader(file)

        for data in csv_reader:
            transactions.append(data)

    return transactions

def divide_into_blocks(transactions, block_size):
    start = 0
    blocks = []

    while start < len(transactions):
        blocks.append(transactions[start : start + block_size])
        start += block_size

    return blocks

def distribute_blocks(blocks):
    datanode_1 = []
    datanode_2 = []
    datanode_3 = []
    for i,block in enumerate(blocks):
        block_id = f"Block {i+1}"
        block_info = (block_id, block)
        if i % 3 == 0:
            datanode_1.append(block_info)
        elif i % 3 == 1:
            datanode_2.append(block_info)
        else:
            datanode_3.append(block_info)

    return datanode_1, datanode_2, datanode_3


def replicate_blocks(datanode_1, datanode_2, datanode_3):
    replicas = {}
    nodes = {
        "DataNode 1": datanode_1,
        "DataNode 2": datanode_2,
        "DataNode 3": datanode_3
    }

    for node_name, blocks in nodes.items():
        for block_id, block in blocks:
            replicas[block_id] = ["DataNode 1", "DataNode 2", "DataNode 3"]
            if block_id not in replicas:
                replicas[block_id] = []

    return replicas

def simulate_failure(replicas, failed_node):
    for block_id, nodes in replicas.items():
        if failed_node in nodes:
            nodes.remove(failed_node)

    return replicas

def main():
    block_size = 1000
    transactions = read_data()
    blocks = divide_into_blocks(transactions, block_size)

    print("Total Transactions :",len(transactions))
    print("Block Size :", block_size)
    print("Total Blocks :",len(blocks))

    datanode_1, datanode_2, datanode_3 = distribute_blocks(blocks)
    print("Datanode_1 :",len(datanode_1)," blocks ")
    print("Datanode_2 :",len(datanode_2)," blocks ")
    print("Datanode_3 :",len(datanode_3)," blocks ")

    replicas = replicate_blocks(datanode_1, datanode_2, datanode_3)
    for dat,data in replicas.items():
        print(dat," : ",data)

    replicas_after_failure = simulate_failure(replicas, "DataNode 1")
    for block_id, nodes in replicas_after_failure.items():
        print(block_id," : ",nodes)
    
    for i,block in enumerate(blocks):
        print("Block ",i+1," : ",len(block)," transactions ")

if __name__ == "__main__":
    main()
