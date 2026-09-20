transactions = [
    {"id": 101, "amount": 2500, "status": "SUCCESS"},
    {"id": 102, "amount": 7500, "status": "SUCCESS"},
    {"id": 103, "amount": 1200, "status": "FAILED"},
    {"id": 104, "amount": 15000, "status": "SUCCESS"},
    {"id": 105, "amount": 3200, "status": "FAILED"}
]

#Lambda
square = lambda x: x * x
print(square(5))

#Adding 10% fee to amount
add_fee = lambda x: x * 1.10
print(f"Total Amount with Fee for 1000 will be: {add_fee(1000)}")

#Map - Extract all using map function
result = list(map(lambda transaction: transaction["amount"], transactions))
print(result)

#Filter - Can filter out whatever data is needed based on condition
result = list(filter(lambda transaction: transaction["amount"] >1000, transactions))
print(result)

amounts = [1000, 5000, 12000, 3000]
result = filter(lambda amount: amount > 3000, amounts)

print(list(result))


#Putting everything together
def process_transactions(transactions):

    success_transactions = [
        t for t in transactions
        if t["status"] == "SUCCESS"
    ]

    failed_transactions = [
        t for t in transactions
        if t["status"] == "FAILED"
    ]

    success_amounts = [
        t["amount"] for t in success_transactions
    ]

    total_success = sum(success_amounts)

    average_success = total_success / len(success_amounts)

    maximum = max(success_amounts)

    minimum = min(success_amounts)

    return {
        "total_transactions": len(transactions),
        "successful_transactions": len(success_transactions),
        "failed_transactions": len(failed_transactions),
        "total_success_amount": total_success,
        "average_success_amount": average_success,
        "maximum_success_amount": maximum,
        "minimum_success_amount": minimum
    }

transResult = process_transactions(transactions)

print(transResult)
