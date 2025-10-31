from collections import UserDict


# Base class for all fields in a contact record
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Represents a contact's name; inherits from Field
class Name(Field):
    def __init__(self, value):
        self.value = value


# Represents a phone number with validation: must be exactly 10 digits
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        self.value = value


class Record:
    def __init__(self, name):
        self.name = Name(name)      # Store the contact's name as a Name object
# Initialize an empty list to hold Phone objects
        self.phones = []

    def add_phone(self, phone_number):
        """Add a new phone number to the contact after validating it."""
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        """Remove a phone number from the contact if it exists."""
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return

    def edit_phone(self, old_phone, new_phone):
        # Check if the old phone number exists in the contact
        old_exists = any(phone.value == old_phone for phone in self.phones)
        if not old_exists:
            raise ValueError(f"Phone {old_phone} not found.")
        # Validate the new phone number by creating a Phone instance
        new_phone_obj = Phone(new_phone)
        # Update the old phone number with the new one
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone_obj.value
                return

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None  # Return None only after checking all phones

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


# Represents an address book that stores multiple contact records
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
