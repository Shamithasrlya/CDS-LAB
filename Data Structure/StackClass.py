"""
    Algorithm: Stack
    Author: Shamitha R
    Date: 22/08/2024
"""       
# Creation of class to perform push and pop in a stack.

class Stack:
    def __init__(self, max_range):
        # Creating an empty stack
        self.stack = []
        self.max_range = max_range

    def push(self, item: object) -> None:
        """ Adds item to a stack"""
        if len(self.stack) < self.max_range:
            self.stack.append(item)
            print(f"'{item}' pushed to stack.")

        else:
            print("Stack overflow.")

    def pop(self):
        """ Removes the last/bottom item of the stack"""
        if self.stack:
            removed_item = self.stack.pop()
            print(f"Item '{removed_item}' popped from stack.")
            return removed_item #Displays the item removed
        else:
            print("Stack is empty. Cannot pop item.") # If the stack is empty, prints the given message.

    def display(self):
        """ Displays the items present in the stack if it is non empty"""
        if self.stack:
            print("Current stack items:", self.stack)
        else:
            print("Stack is empty.") #Message printed if the stack is empty.

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
    """Main function of stack."""
    max_range = int(input("Enter the range of the stack: ")) #Maximum range of the stack
    my_stack = Stack(max_range)

    while True: 
        """Options for the operations to be performed."""
        print("\n1. Push item")
        print("2. Pop item")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1": #Push/Append item
                item = my_stack.input_1("Enter the item: ")
                my_stack.push(item)
                my_stack.display()

        elif choice == "2": #Pop an item.
            my_stack.pop()
            my_stack.display()

        elif choice == "3": #Exiting the program.
            print("Exit.")
            break

        else:
            print("Enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
