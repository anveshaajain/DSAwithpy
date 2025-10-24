class StackQueue:

    def __init__(self):
      self.stack1=[]
      self.stack2=[]


    def enqueue(self,item):
        self.stack1.append(item)
        print(f"Enqueued {item} to queue.")

    
    def dequeue(self):
        # If stack2 is empty, move all items from stack1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # If stack2 is still empty, queue is empty
        if not self.stack2:
            print("Queue is empty")
            return None

        # Pop from stack2
        return self.stack2.pop()

    def is_empty(self):
        return not (self.stack1 or self.stack2)


if __name__=='__main__':
    q=StackQueue()

    while True:

        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Check if empty")
        print("4. Exit")
        choice=int(input("Enter your choice: "))

        if choice==1:
            item=int(input("Enter item to enqueue: "))
            q.enqueue(item)

        elif choice==2:
            dequeued_item=q.dequeue()
            if dequeued_item is not None:
                print(f"Dequeued {dequeued_item} from queue.")

        elif choice==3:
            if q.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")

        elif choice==4:
            break    