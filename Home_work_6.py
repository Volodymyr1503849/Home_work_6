
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must be 10 digits long!")
        super().__init__(phone)            

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None
       
    def remove_phone(self, phone):
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError("Phone number is incorect")
                 
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self,record):
           self.data[record.name.value] = record

    def find(self,name):
          if name in self.data:
              return self.data[name] 
                 
    def delete(self,name):
        del self.data[name] 

    def __str__(self):
        a=""
        for i in self.data:
            a = a + f"{self.data[i]}" + "\n"
        return a
