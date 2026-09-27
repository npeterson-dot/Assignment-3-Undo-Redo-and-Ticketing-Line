from node import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None

        removed_node = self.top
        self.top = self.top.next
        return removed_node.value

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None

    def print_stack(self):
        current = self.top

        if not current:
            print("Stack is empty")
            return

        while current:
            print(f"- {current.value}")
            current = current.next


def undo_redo_manager():
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            redo_stack = Stack()
            print(f"Action performed: {action}")

        elif choice == "2":
            action = undo_stack.pop()

            if action is not None:
                redo_stack.push(action)
                print(f"Undid action: {action}")
            else:
                print("No actions to undo")

        elif choice == "3":
            action = redo_stack.pop()

            if action is not None:
                undo_stack.push(action)
                print(f"Redid action: {action}")
            else:
                print("No actions to redo")

        elif choice == "4":
            print("Undo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            print("Redo Stack:")
            redo_stack.print_stack()

        elif choice == "6":
            print("Exiting undo/redo manager.")
            break

        else:
            print("Invalid option. Please choose 1-6.")


undo_redo_manager()