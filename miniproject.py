# To-Do List Application

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title):
        """Add a task with a title."""
        self.tasks[title] = 'Incomplete'

    def view_tasks(self):
        """View the list of tasks with their titles and statuses."""
        if not self.tasks:
            print("No tasks to display.")
        for title, status in self.tasks.items():
            print(f"{title}: {status}")

    def mark_as_complete(self, title):
        """Mark a task as complete."""
        if title in self.tasks:
            self.tasks[title] = 'Complete'
            print(f"Task '{title}' marked as complete.")
        else:
            print(f"Task '{title}' not found.")

    def delete_task(self, title):
        """Delete a task."""
        if title in self.tasks:
            del self.tasks[title]
            print(f"Task '{title}' deleted.")
        else:
            print(f"Task '{title}' not found.")

    def run(self):
        """Run the To-Do List Application."""
        while True:
            print("\nWelcome to the To-Do List App!\n")
            print("Menu:")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Mark a task as complete")
            print("4. Delete a task")
            print("5. Quit")

            choice = input("Select an option: ")

            try:
                if choice == '1':
                    title = input("Enter the title of the task: ")
                    self.add_task(title)
                elif choice == '2':
                    self.view_tasks()
                elif choice == '3':
                    title = input("Enter the title of the task to mark as complete: ")
                    self.mark_as_complete(title)
                elif choice == '4':
                    title = input("Enter the title of the task to delete: ")
                    self.delete_task(title)
                elif choice == '5':
                    print("Thank you for using the To-Do List App!")
                    break
                else:
                    print("Invalid option. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                print("Operation completed.")

# Create an instance of the ToDoList and run the application
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
