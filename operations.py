from data_structures import Stack, Queue, PriorityQueue

def determine_data_structure(operations):
    stack = Stack()
    queue = Queue()
    priority_queue = PriorityQueue()

    is_stack = True
    is_queue = True
    is_priority_queue = True

    for op, x in operations:
        print(f"Operation: {op}, Value: {x}")
        
        if op == "push":
            if is_stack:
                stack.push(x)
                print(f"Stack after push: {stack.items}")
            if is_queue:
                queue.enqueue(x)
                print(f"Queue after enqueue: {queue.items}")
            if is_priority_queue:
                priority_queue.insert(x)
                print(f"PriorityQueue after insert: {priority_queue.items}")
        elif op == "pop":
            if is_stack:
                if stack.is_empty() or stack.pop() != x:
                    is_stack = False
                print(f"Stack after pop: {stack.items}")
            if is_queue:
                if queue.is_empty() or queue.dequeue() != x:
                    is_queue = False
                print(f"Queue after dequeue: {queue.items}")
            if is_priority_queue:
                if priority_queue.is_empty() or priority_queue.extract_max() != x:
                    is_priority_queue = False
                print(f"PriorityQueue after extract_max: {priority_queue.items}")

    print(f"Final States: Stack={is_stack}, Queue={is_queue}, PriorityQueue={is_priority_queue}")

    if is_stack and not is_queue and not is_priority_queue:
        return "stack"
    elif is_queue and not is_stack and not is_priority_queue:
        return "queue"
    elif is_priority_queue and not is_stack and not is_queue:
        return "priority queue"
    else:
        return "impossible"
