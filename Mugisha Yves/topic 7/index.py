import time

def create_node(name):
    return {
        "name": name,
        "children": [], 
        "transactions": [] 
    }

def add_transaction(wallet, parent_name, transaction_description, amount, priority):
    parent_node = find_node(wallet, parent_name)
    if parent_node:
        timestamp = time.time() 
        transaction = {"description": transaction_description, "amount": amount, "priority": priority, "timestamp": timestamp}
        parent_node["transactions"].append(transaction)
        print(f"Transaction added under {parent_name}: {transaction_description} with priority {priority}")
    else:
        print(f"Node {parent_name} not found.")

def find_node(wallet, node_name):
    if wallet["name"] == node_name:
        return wallet
    for child in wallet["children"]:
        found_node = find_node(child, node_name)
        if found_node:
            return found_node
    return None

def merge(left, right):
    result = []
    while left and right:
        if left[0]['priority'] <= right[0]['priority']:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

def merge_sort(transactions):
    if len(transactions) <= 1:
        return transactions
    middle = len(transactions) // 2
    left_half = merge_sort(transactions[:middle])
    right_half = merge_sort(transactions[middle:])
    return merge(left_half, right_half)

def display_wallet(wallet):
    print("Wallet Structure (Sorted by Priority):")
    display_node(wallet, 0)

def display_node(node, level):
    print(" " * level * 2 + f"Node: {node['name']}")
    if node["transactions"]:
        print(" " * (level + 1) * 2 + "Transactions (Sorted):")
        sorted_transactions = merge_sort(node["transactions"])
        for transaction in sorted_transactions:
            print(" " * (level + 2) * 2 + f"- {transaction['description']} | Priority: {transaction['priority']} at {time.ctime(transaction['timestamp'])}")
    for child in node["children"]:
        display_node(child, level + 1)

wallet = create_node("Wallet")

wallet['children'].append(create_node("Credit Card"))
wallet['children'].append(create_node("Store A"))

add_transaction(wallet, "Credit Card", "Paid $10 to Store A", 10, priority=2)
add_transaction(wallet, "Credit Card", "Paid $20 to Store B", 20, priority=1)
add_transaction(wallet, "Store A", "Paid $5 for groceries", 5, priority=3)

display_wallet(wallet)
