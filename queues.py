
class ListQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)  

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  
        else:
            print("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

if __name__=='__main__':

    q=ListQueue()

    while True:

        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Exit")
        choice=int(input("Enter your choice: "))

        if choice==1:
            item=int(input("Enter item to enqueue: "))
            q.enqueue(item)
            print(f"Enqueued {item} to queue.")

        elif choice==2:
            dequeued_item=q.dequeue()


        elif choice==3:
            front_item=q.peek()
            if front_item is not None:
                print(f"Front item is {front_item}.")



        elif choice==4:
            if q.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")

                
        elif choice==5:
            break
        else:
            print("Invalid choice. Please try again.")   

