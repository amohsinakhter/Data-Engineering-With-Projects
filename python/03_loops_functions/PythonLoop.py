transactions = [
    {"id": 101, "amount": 2500, "status": "SUCCESS"},
    {"id": 102, "amount": 7500, "status": "SUCCESS"},
    {"id": 103, "amount": 1200, "status": "FAILED"},
    {"id": 104, "amount": 3500, "status": "SUCCESS"},
    {"id": 105, "amount": 4200, "status": "FAILED"}
]

for transaction in transactions:
    print(transaction)