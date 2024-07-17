class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title, priority, due_date):
        """Add a task with a title, priority, and due date."""
        if title not in self.tasks:
            self.tasks[title] = {'status': 'Incomplete', 'priority': priority, 'due_date': due_date}
            print(f"Task '{title}' added successfully.")
        else:
            print(f"Task '{title}' already exists.")

    def view_tasks(self):
        """View the list of tasks with their titles, statuses, priorities, and due dates."""
        if not self.tasks:
            print("No tasks to display.")
        for title, details in self.tasks.items():
            status_color = "\033[92m" if details['status'] == 'Complete' else "\033[91m"
            print(f"{title}: {status_color}{details['status']}\033[0m, Priority: {details['priority']}, Due: {details['due_date']}")

    def mark_as_complete(self, title):
        """Mark a task as complete."""
        if title in self.tasks:
            self.tasks[title]['status'] = 'Complete'
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
                    priority = input("Enter the priority of the task (High, Medium, Low): ")
                    due_date = input("Enter the due date (e.g., YYYY-MM-DD): ")
                    self.add_task(title, priority, due_date)
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
