class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:  # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:  # Queue became empty
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data


if __name__ == '__main__':
    q = Queue()

    while True:
        print("\nSelect one operation from below")
        print("1. Enqueue\n2. Dequeue\n3. Peek\n4. Check if empty\n5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            item = int(input("Enter item to enqueue: "))
            q.enqueue(item)
            print(f"Enqueued {item} to queue.")

        elif choice == 2:
            dequeued_item = q.dequeue()
            if dequeued_item is not None:
                print(f"Dequeued {dequeued_item} from queue.")

        elif choice == 3:
            front_item = q.peek()
            if front_item is not None:
                print(f"Front item is {front_item}.")

        elif choice == 4:
            if q.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")