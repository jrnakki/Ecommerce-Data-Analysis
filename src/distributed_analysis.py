import csv

def read_data():
    transactions = []
    with open("data/transactions.csv", "r", newline="") as file:
        csv_reader = csv.DictReader(file)

        for data in csv_reader:
            transactions.append(data)

    return transactions

def divide_into_chunks(transactions, chunk_size):
    start = 0
    chunks = []
    while start < len(transactions):
        chunks.append(transactions[start:start + chunk_size])
        start += chunk_size

    return chunks

def process_chunk(chunk):
    total_transactions = len(chunk)
    total_revenue = 0
    total_quantity = 0
    for data in chunk:
        total_revenue += int(data["quantity"]) * int(data["price"])
        total_quantity += int(data["quantity"])

    chunk_analysis = {
        "total_transactions": total_transactions,
        "total_revenue": total_revenue,
        "total_quantity": total_quantity
    }
    return chunk_analysis

def reduce_results(results):
    grand_total_transactions = 0
    grand_total_revenue = 0
    grand_total_quantity = 0

    for data in results:
        grand_total_transactions += data["total_transactions"]
        grand_total_revenue += data["total_revenue"]
        grand_total_quantity += data["total_quantity"]

    complete_analysis = {
        "grand_total_transactions": grand_total_transactions,
        "grand_total_revenue": grand_total_revenue,
        "grand_total_quantity": grand_total_quantity
    }

    return complete_analysis

def main():
    chunk_size = 1000
    transactions = read_data()
    chunks = divide_into_chunks(transactions, chunk_size)
    print("Total Transactions:", len(transactions))
    print("Chunk Size:", chunk_size)
    print("Total Chunks:", len(chunks))

    results = []
    for i, chunk in enumerate(chunks):
        chunk_analysis = process_chunk(chunk)
        print("Chunk ",i+1,":",len(chunk)," transactions \n"
        "And its result is :",chunk_analysis,"\n")
        results.append(chunk_analysis)

    print("Final_analysis : ",reduce_results(results))

if __name__ == "__main__":
    main()
