import csv

def read_data():
    with open("data/transactions.csv", "r", newline="") as file:
        transactions = []
        csv_reader = csv.DictReader(file)

        for data in csv_reader:
            transactions.append(data)

    return transactions

def analyse_product_patterns(transactions):
    product_sales = {
        "Laptop" : 0, 
        "Mobile" : 0, 
        "Headphone" : 0, 
        "Keyboard" : 0, 
        "Mouse" : 0
    }

    for data in transactions:
        product_sales[data["product"]] += int(data["quantity"])

    return product_sales

def calculate_sales_percentage(product_sales):
    total_sales = sum(product_sales.values())
    product_percentage = {
        "Laptop" : 0, 
        "Mobile" : 0, 
        "Headphone" : 0, 
        "Keyboard" : 0, 
        "Mouse" : 0
    }

    for product,data in product_sales.items():
        product_percentage[product] = (data / total_sales)*100

    return product_percentage

def analyse_customer_spending(transactions):
    customer_spending = {}
    for data in transactions:
        if data["customer_ID"] not in customer_spending:
            customer_spending[data["customer_ID"]] = 0
        else:
            customer_spending[data["customer_ID"]] += int(data["quantity"])* int(data["price"])

    return customer_spending

def find_top_customer(customer_spending):
    max_spend_customer_id = max(customer_spending, key=customer_spending.get)
    amount_spend = customer_spending[max_spend_customer_id]
    max_details = {max_spend_customer_id : amount_spend}

    return max_details

def find_bottom_customer(customer_spending):
    min_spend_customer_id = min(customer_spending, key=customer_spending.get)
    amount_spend = customer_spending[min_spend_customer_id]
    min_details = {min_spend_customer_id : amount_spend}

    return min_details

def calculate_average_spending(customer_spending):
    total_spendings = sum(customer_spending.values())
    total_transactions = len(customer_spending)
    avg_spending = total_spendings/total_transactions
    return avg_spending

def find_high_value_customers(customer_spending):
    high_value_customers = {}
    for customer_id, spending in customer_spending.items():
        if spending > 500000:
            high_value_customers[customer_id] = spending

    return high_value_customers

def analyse_payment_methods(transactions):
    payment_methods = {
    "UPI" : 0,
    "Card" : 0,
    "Cash" : 0
    }

    for data in transactions:
        payment_methods[data["payment_Method"]] += 1

    return payment_methods

def calculate_payment_percentage(payment_methods):
    total_transactions = sum(payment_methods.values())
    payment_percent = {
    "UPI" : 0,
    "Card" : 0,
    "Cash" : 0
    }
    for method,pay in payment_methods.items():
        payment_percent[method] = round((pay/total_transactions)*100,2)

    return payment_percent

def calculate_high_value_revenue(high_value_customers):
    total_spent = sum(high_value_customers.values())
    return total_spent

def calculate_high_value_contribution(total_spent, customer_spending):
    total_revenue = sum(customer_spending.values())
    high_value_cotribution = round((total_spent/total_revenue)*100,2)
    return high_value_cotribution

def generate_data_mining_report(product_sales, payment_methods, max_details, high_value_customers, total_spent, high_value_cotribution):
    print("\n \n")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("                                                        REPORT                                                             ")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("\n \n")

    most_selling_product = max(product_sales, key=product_sales.get)
    units_sold = product_sales[most_selling_product]
    print(" Most selling product is :",most_selling_product,"and its units sold is :",units_sold)

    least_selling_product = min(product_sales, key=product_sales.get)
    lunits_sold = product_sales[least_selling_product]
    print("\n Least selling product is :",least_selling_product,"and its units sold is :",lunits_sold)

    most_used_payment_method = max(payment_methods, key=payment_methods.get)
    transaction_count = payment_methods[most_used_payment_method]
    print("\n Most used payment method is :",most_used_payment_method,"and its used :",transaction_count,"times \n")

    for customer_id, amount in max_details.items():
        print(" Highest spending customer is :",customer_id,"and amount spend is :",amount)

    count_high = 0
    for i in high_value_customers:
        count_high += 1
    print("\n Number of high value customers are :",count_high)

    print("\n Total revenue from high value customers is :",total_spent)

    print("\n Their percentage contribution for total revenue is :",high_value_cotribution," %")



def main():
    transactions = read_data()

    product_sales = (analyse_product_patterns(transactions))
    print("Product Sales :",product_sales)

    product_percentage = calculate_sales_percentage(product_sales)
    print("Product Percentage :",product_percentage)

    print("Max product selled :",max(product_sales, key=product_sales.get))
    print("Min product selled :",min(product_sales, key=product_sales.get))

    customer_spending = analyse_customer_spending(transactions)
    for cusid,money in customer_spending.items():
        print("Customer :",cusid," money spent :",money)

    max_details = find_top_customer(customer_spending)
    print(max_details)

    min_details = find_bottom_customer(customer_spending)
    print(min_details)

    average_spending = calculate_average_spending(customer_spending)
    print("Average Spending :",average_spending)

    high_value_customers = (find_high_value_customers(customer_spending))
    print(high_value_customers)

    payment_methods = analyse_payment_methods(transactions)
    print("Payment methods :",payment_methods)

    payment_percent = calculate_payment_percentage(payment_methods)
    print("Payment percentage :",payment_percent)

    total_spent = calculate_high_value_revenue(high_value_customers)
    print("Total money spent by high value customers is :",total_spent)

    high_value_cotribution = calculate_high_value_contribution(total_spent, customer_spending)
    print("High value customer gave ",high_value_cotribution,"%"" of contribution in total revenue")

    generate_data_mining_report(product_sales, payment_methods, max_details, high_value_customers, total_spent, high_value_cotribution)

if __name__ == "__main__":
    main()
