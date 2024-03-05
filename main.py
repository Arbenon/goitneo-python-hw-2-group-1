

def input_error(func):                
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Wrong value. Give me command, name and phone number."
    return inner

def command_error(func):               
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me command, name and phone number."
    return inner

@command_error
def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        user_input = input("Wish to change user's number? y/n ")
        if user_input == 'y':
            contacts[name] = phone
            return "Contact changed."
        else:
            return "Contact isn't changed."
    else:
        contacts[name] = phone
        return "Contact added."


def main():
    contacts = {}
    print("Welcome! This is your assistant.")
    while True:
        user_input = input('Enter your command: ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(add_contact(args, contacts))
        elif command == "all":
            print('All contacts:')
            for name, phone in contacts.items():
                print("|{:^15}|{:^15}|".format(name, phone))
        else:
            print('Invalid command.')

if __name__ == "__main__":
    main()




