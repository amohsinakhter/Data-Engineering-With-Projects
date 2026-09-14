transactions = [
    {"id": 101, "amount": 2500, "status": "SUCCESS"},
    {"id": 102, "amount": 7500, "status": "SUCCESS"},
    {"id": 103, "amount": 1200, "status": "FAILED"},
    {"id": 104, "amount": 15000, "status": "SUCCESS"},
    {"id": 105, "amount": 3200, "status": "FAILED"}
]


totalAmount =   sum(transaction["amount"] for transaction in transactions)
print(f"Total Amount: {totalAmount}")

average = totalAmount / len(transactions)
print(f"Average Amount: {average}")

maximumAmount = max(transaction["amount"] for transaction in transactions)
print(f"Maximum Amount: {maximumAmount}")

minimumAmount = min(transaction["amount"] for transaction in transactions)
print(f"Minimum Amount: {minimumAmount}")

numberOfTransactions = len(transactions)
print(f"Number of transactions: {numberOfTransactions}")

total_success = 0

for transaction in transactions:
    if transaction["status"] == "SUCCESS":
        total_success = total_success + transaction["amount"]

print(f"Total Success Transaction Amount: {total_success}")

uniqueStatus = set(transaction["status"] for transaction in transactions)
print(f"Unique Status: {uniqueStatus}")
