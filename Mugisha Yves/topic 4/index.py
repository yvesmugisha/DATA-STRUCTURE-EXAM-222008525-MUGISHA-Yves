head = None  
tail = None  
max_orders = 5  
order_count = 0 

def add_order(order_id, amount, merchant):
    global head, tail, order_count

    new_node = {'order_id': order_id, 'amount': amount, 'merchant': merchant, 'prev': None, 'next': None}

    if head is None: 
        head = tail = new_node
    else:
        tail['next'] = new_node
        new_node['prev'] = tail
        tail = new_node

    order_count += 1

    if order_count > max_orders:
        remove_oldest_order()

    print(f"Order added: ID={order_id}, Amount={amount}, Merchant={merchant}")

def remove_oldest_order():
    global head, order_count
    if head is None:
        print("No orders to remove.")
        return

    print(f"Removing oldest order: ID={head['order_id']}, Amount={head['amount']}, Merchant={head['merchant']}")
    
    head = head['next']
    if head:
        head['prev'] = None
    else:
        tail = None

    order_count -= 1

def display_orders():
    if head is None:
        print("No orders available.")
        return

    print("Current Orders:")
    current = head
    while current:
        print(f"ID={current['order_id']}, Amount={current['amount']}, Merchant={current['merchant']}")
        current = current['next']

def clear_orders():
    global head, tail, order_count
    head = tail = None
    order_count = 0
    print("All orders cleared.")

def get_total_balance():
    total = 0
    current = head
    while current:
        total += current['amount']
        current = current['next']
    print(f"Total balance: ${total}")
    return total

add_order(1, 20, "Coffee Shop")
add_order(2, 50, "Grocery Store")
add_order(3, 30, "Restaurant")
add_order(4, 15, "Book Store")
add_order(5, 40, "Clothing Store")
add_order(6, 25, "Electronics Store")  

display_orders()
get_total_balance()
clear_orders()
display_orders()

