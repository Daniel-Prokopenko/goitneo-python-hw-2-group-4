from collections import UserDict
import re


def is_correct(number):
    """Checks if given number is ten digits"""
    return re.fullmatch(r"\d{10}", number)


class Field:
    """Represents a contact name or a phone number"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Represents a contact`s name"""

    def __str__(self):
        return str(self.value)


class Phone(Field):
    """Represents a contact`s phone number"""

    def __str__(self):
        return str(self.value)


class Record:
    """Represents a contact that is going to be added"""

    def __init__(self, name: str):
        self.name = Name(name.title())
        self.phones = []

    def add_phone(self, number: str):
        """Adds the number to the record"""
        if is_correct(number):
            self.phones.append(Phone(number))
            print("Number added.")
        else:
            print("Wrong format.")

    def delete_phone(self, number: str):
        """Deletes the number from the record"""
        deleted = False  # For prints to work properly
        for phone in self.phones:
            if phone.value == number:
                del self.phones[self.phones.index(phone)]
                print("Number deleted.")
                deleted = True
                break
        if not deleted:
            print("No such number.")

    def find_phone(self, number_to_find: str):
        """Finds the phone number in the record"""
        phones_found = list(
            filter(lambda phone: number_to_find in phone.value, self.phones)
        )
        if phones_found:
            print(f"Phones found: {', '.join(phone.value for phone in phones_found)}")
        else:
            print("No such numbers.")

    def edit_phone(self, current_number: str, new_number: str):
        """Changes the phone number if such is in the record"""
        if is_correct(new_number):
            edited = False  # For prints to work properly
            for phone in self.phones:
                if phone.value == current_number:
                    phone.value = new_number
                    print("Number changed.")
                    edited = True
                    break
            if not edited:
                print("No such number.")
        else:
            print("Wrong format.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Represents an address book filled with contacts"""

    def add_record(self, rec: Record):
        """Adds contact to the address book"""
        self.data[rec.name] = rec
        print("Contact added.")

    def find(self, name: str):
        """Finds contact in the address book"""
        for contact in self.data:
            if name == contact.value:
                return self.data[contact]
        print("No such contact.")

    def delete(self, name: str):
        """Deletes contact from the address book"""
        deleted = False  # For prints to work properly
        for contact in self.data:
            if name == contact.value:
                del self.data[contact]
                print("Contact deleted.")
                deleted = True
                break
        if not deleted:
            print("No such contact.")

    def contacts(self):
        """Prints all contacts from the address book"""
        if self.data:
            for _, rec in self.data.items():
                print(rec)
        else:
            print("No contacts.")
