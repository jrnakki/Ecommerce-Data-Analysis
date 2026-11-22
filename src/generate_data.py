import csv
import random

products = ["Laptop", "Mobile", "Headphone", "Keyboard", "Mouse"]
methods = ["UPI", "Card", "Cash"]
prices = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Headphone": 2000,
    "Keyboard": 1500,
    "Mouse": 800
}

def generate_data():
    with open("data/transactions.csv", "w", newline = "") as file:
        csv_writer = csv.writer(file)
    
        csv_writer.writerow(["transaction_ID", "customer_ID", "product", "quantity", "price", "payment_Method"])
        
        for i in range(10000):
            transaction_ID = i+1
            customer_ID = random.randint(1,1000)
            product = random.choice(products)
            quantity = random.randint(1,5)
            price = prices[Product]
            payment_Method = random.choice(methods)
            csv_writer.writerow([Transaction_ID, Customer_ID, Product, Quantity, Price, Payment_Method])

if __name__ == "__main__":
    generate_data()
