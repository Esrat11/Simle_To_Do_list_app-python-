tasks = []
print("-----Welcome to To-Do App----")

total_task = int(input("Enter how many tasks you want to add = "))
for i in range(1, total_task + 1):
    task_name = input(f"Enter task {i} = ")
    tasks.append(task_name)

print(f"Today's tasks are\n{tasks}")

while True:
    operation = int(input("Enter:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n"))

    if operation == 1:
        add = input("Enter the task you want to add = ")
        tasks.append(add)
        print(f"Task '{add}' has been successfully added.")

    elif operation == 2:
        updated_val = input("Enter the task name you want to update = ")
        if updated_val in tasks:
            up = input("Enter new task = ")
            ind = tasks.index(updated_val)
            tasks[ind] = up
            print(f"Task '{updated_val}' updated to '{up}'.")
        else:
            print("Task not found!")

    elif operation == 3:
        delete_task = input("Enter the task you want to delete = ")
        if delete_task in tasks:
            tasks.remove(delete_task)
            print(f"Task '{delete_task}' has been deleted.")
        else:
            print("Task not found!")

    elif operation == 4:
        print(f"Current tasks: {tasks}")

    elif operation == 5:
        print("Exit_To_Do App")
        break 
