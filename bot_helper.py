import re


def input_error(func):
    """Checks if input format is correct and messages if not so"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Wrong format."

    return inner


def parse_input(user_input):
    """Defines command and arguments"""
    while not user_input:  # In case empty input was given
        user_input = input("Enter a command: ")
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    """Adds contact to contact list or changes the existing one"""
    name, phone_number = args
    if name in contacts:
        return "Contact is already in list."
    if re.fullmatch(r"[+]?\d+", phone_number):
        contacts[name] = phone_number
    else:
        return "Wrong format."
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """Changes contact`s phone number if such contact is in contact list"""
    name, phone_number = args
    if name in contacts:
        contacts[name] = phone_number
        return "Contact updated."
    return "No such contact."


@input_error
def phone(args, contacts):
    """Shows contact`s phone number if such contact is in contact list"""
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "No such contact."


@input_error
def show_all(contacts):
    """Shows all contacts in contact list"""
    if contacts:
        return "\n".join(
            [f"{name}: {number}" for name, number in sorted(contacts.items())]
        )
    return "No contacts."


@input_error
def delete_contact(args, contacts):
    """Deletes contact if it is in contact list"""
    name = args[0]
    if name in contacts:
        del contacts[name]
        return "Contact deleted."
    return "No such contact."


def main():
    """Defines what function to run according to command"""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        args = (None, None)
        command, *args = parse_input(user_input)
        if command in ["close", "exit", "goodbye"]:
            print("Goodbye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone(args, contacts))
        elif command == "delete":
            print(delete_contact(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
