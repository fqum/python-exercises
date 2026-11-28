contacts = {}

while True:
    command = input("add / find / list / quit: ").strip().lower()

    if command == "add":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Saved")
    elif command == "find":
        name = input("Name: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Not found")
    elif command == "list":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif command == "quit":
        break
    else:
        print("Unknown command")
