


cnt = 0
todos = []
while True:
    for i in range(len(todos)):
        print(f"{i+1}) {todos[i]}")
    print("****************************************************")
    print("Enter a command. Type 'h' for help: ")
    cmd = input("> ")
    if cmd == 'q':
        break
    elif cmd.isnumeric():
        num = int(cmd)
        if num-1 >= len(todos):
            print("No TODO with this index")
        else:
            todos.pop(num-1)
    else:
        todos.append(cmd)




