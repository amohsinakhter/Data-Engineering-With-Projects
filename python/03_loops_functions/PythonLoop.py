transactions = [
    {"id": 101, "amount": 2500, "status": "SUCCESS"},
    {"id": 102, "amount": 7500, "status": "SUCCESS"},
    {"id": 103, "amount": 1200, "status": "FAILED"},
    {"id": 104, "amount": 3500, "status": "SUCCESS"},
    {"id": 105, "amount": 4200, "status": "FAILED"}
]

#Loop
total = 0
for transaction in transactions:
    print(f"All transactions: {transaction}")

for transaction in transactions:
    if transaction["status"] == "SUCCESS":
        total = total + transaction["amount"]
print(f"Total Success: {total}")

#List Comprehension
successTrasactions = [t for t in transactions if t["status"] == "SUCCESS"]
print(successTrasactions)

failTrasactions = [t for t in transactions if t["status"] == "FAILED"]
print(failTrasactions)

#Function
def calculate_success_total(transactions):

    totalSuccess = 0

    for transaction in transactions:
        if transaction["status"] == "SUCCESS":
            totalSuccess += transaction["amount"]

    return totalSuccess

result = calculate_success_total(transactions)
print(f"Total Success: {result}")

