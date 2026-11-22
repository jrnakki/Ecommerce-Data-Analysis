import csv

def analyse_data():
    total_transactions = 0
    revenue = 0
    products = {
        "Laptop" : 0, 
        "Mobile" : 0, 
        "Headphone" : 0, 
        "Keyboard" : 0, 
        "Mouse" : 0
    }
    
    product_revenue = {
        "Laptop": 0,
        "Mobile": 0,
        "Headphone": 0,
        "Keyboard": 0,
        "Mouse": 0
    }
    
    payment = {
        "UPI" : 0,
        "Card" : 0,
        "Cash" : 0
    }

    with open ("data/transactions.csv", "r", newline = "") as file:
        csv_reader = csv.DictReader(file)
    
        for data in csv_reader:
            total_transactions += 1
            revenue += int(data["Quantity"]) * int(data["Price"])
            product_revenue[data["Product"]] += int(data["Quantity"]) * int(data["Price"])
            products[data["Product"]] += int(data["Quantity"])
            payment[data["Payment_Method"]] += 1

    if total_transactions > 0 :
        avg_transaction_value = revenue / total_transactions
    else :
        avg_transaction_value = 0
    
    
    print(payment)
    print("Total Transactions : ",total_transactions)
    print("Total Revenue : ",revenue)
    print("Individual Product Revenue : ",product_revenue)
    print("Highest Revenue Product : ",max(product_revenue, key = product_revenue.get))
    print("Total Quantity sold : ",sum(products.values()))
    print("Product Wise Quantity : ",products)
    print("Most Popular Product :",max(products, key = products.get))
    print("Most Popular Payment Method : ",max(payment, key = payment.get))
    print("Average Transaction Value : ",revenue / total_transactions)
    print("Percentage of UPI Transactions : ",(payment["UPI"]/total_transactions)*100)
    print("Least popular method : ",min(payment, key = payment.get))

if __name__ == "__main__":
    analyse_data()
