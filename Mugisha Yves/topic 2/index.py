transactions = []
queue = [None] * 5 
front = -1 
rear = -1  
max_size = 5
def add_transaction(transaction):
    transactions.append(transaction)
    print(f"Transaction added: {transaction}")
def display_transactions():
    if not transactions:
        print("No transactions available.")
        return
    print("Transaction History:")
    for t in transactions:
        print(f"- {t}")
def is_full():
    return (rear + 1) % max_size == front
def is_empty():
    return front == -1
def enqueue_payment(payment):
    global front, rear
    if is_full():
        print("Payment queue is full. Cannot add new payment.")
        return
    if is_empty():
        front = 0
    rear = (rear + 1) % max_size
    queue[rear] = payment
    print(f"Payment enqueued: {payment}")
def dequeue_payment():
    global front, rear
    if is_empty():
        print("Payment queue is empty. No payment to process.")
        return None
    payment = queue[front]
    if front == rear: 
        front = rear = -1
    else:
        front = (front + 1) % max_size
    print(f"Payment dequeued: {payment}")
    return payment
def display_queue():
    if is_empty():
        print("Payment queue is empty.")
        return
    print("Current Payment Queue:")
    i = front
    while True:
        print(f"- {queue[i]}")
        if i == rear:
            break
        i = (i + 1) % max_size
add_transaction("Paid $10 to Store A")
add_transaction("Paid $5 to Store B")
display_transactions()
enqueue_payment("Payment 1")
enqueue_payment("Payment 2")
enqueue_payment("Payment 3")
enqueue_payment("Payment 4")
enqueue_payment("Payment 5")
enqueue_payment("Payment 6")
display_queue()

dequeue_payment()
dequeue_payment()
display_queue()
