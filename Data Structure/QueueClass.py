"""
    Algorithm: Queue
    Author: Shamitha R
    Date: 23/08/2024
"""       
# Creation of class to perform enqueue and dequeue in a queue.

class Queue:
    def __init__(self):
        # Creating an empty queue
        self.queue = []

    def enqueue(self, item: object) -> None:
        """ Adds item to a queue"""
        self.queue.append(item)
        print(f"'{item}' pushed to queue.")

    def dequeue(self):
        """ Removes the first item of the queue"""
        if self.queue:
            removed_item = self.queue.pop(0)
            print(f"Item '{removed_item}' popped from queue.")
            return removed_item #Displays the item removed
        else:
            print("Queue is empty. Cannot remove item.") # If the queue is empty, prints the given message.

    def display(self):
        """ Displays the items present in the queue if it is non empty"""
        if self.queue:
            print("Current queue items:", self.queue)
        else:
            print("Queue is empty.") #Message printed if the stack is empty.

    def input_1(self,prompt):
        """
        To get valid input, Cannot enter blank spaces.
        prompt : The message to be displayed to the user.

        """
        while True:
            value = input(prompt)
            if value: # To ensure that input is non empty.
                return value
            else:
                print("Invalid input")

def main():
    """Main function of queue."""
    my_queue = Queue()

    while True: 
        """Options for the operations to be performed."""
        print("\n1. Add item")
        print("2. Remove item")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1": #Push/Append item
                item = my_queue.input_1("Enter the item: ")
                my_queue.enqueue(item)
                my_queue.display()

        elif choice == "2": #Pop an item.
            my_queue.dequeue()
            my_queue.display()

        elif choice == "3": #Exiting the program.
            print("Exit.")
            break

        else:
            print("Enter a number between 1 and 3.")
            
if __name__ == "__main__":
    main()
