wallet_transactions = []
def add_payment(amount, merchant):
    transaction = {
        'amount': amount,
        'merchant': merchant
    }
    wallet_transactions.append(transaction)
    print(f"Payment added: {amount} to {merchant}")
def display_transactions():
    if not wallet_transactions:
        print("No transactions available.")
        return
    print("Transaction History:")
    for idx, transaction in enumerate(wallet_transactions, 1):
        print(f"{idx}. Paid ${transaction['amount']} to {transaction['merchant']}")

def get_total_balance():
    total = sum(transaction['amount'] for transaction in wallet_transactions)
    print(f"Total balance spent: ${total}")
    return total

def find_transactions_by_merchant(merchant_name):
    filtered_transactions = [t for t in wallet_transactions if t['merchant'] == merchant_name]
    if not filtered_transactions:
        print(f"No transactions found for merchant: {merchant_name}")
    else:
        print(f"Transactions with {merchant_name}:")
        for t in filtered_transactions:
            print(f"- Paid ${t['amount']}")

def clear_transactions():
    wallet_transactions.clear()
    print("All transactions cleared.")

add_payment(20, "Coffee Shop")
add_payment(50, "Grocery Store")
add_payment(15, "Coffee Shop")

display_transactions()

get_total_balance()

find_transactions_by_merchant("Coffee Shop")

clear_transactions()

display_transactions()
