# from functions import get_todo_list, write_todo_list
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todo_list = functions.get_todo_list()

        todo_list.append(todo + "\n")

        functions.write_todo_list(todo_list)

    elif user_action.startswith("show"):

        todo_list = functions.get_todo_list()
        
        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todo_list = functions.get_todo_list()

            new_todo = input("Enter a new to-do: ")
            todo_list[number] = new_todo + "\n"

            functions.write_todo_list(todo_list)
        except ValueError:
            print("Please select the number of the item to edit.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todo_list = functions.get_todo_list()
            
            index = number - 1
            todo_to_remove = todo_list[index].strip("\n")
            todo_list.pop(index)

            functions.write_todo_list(todo_list)

            message = f"To-do {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye!")