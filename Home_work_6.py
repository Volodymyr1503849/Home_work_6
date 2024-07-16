from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, name):
        self.value = name

class Phone(Field):
    def __init__(self, phone):
        self.value = phone[-10:]

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    def find_phone(self,phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None
       
    def remove_phone(self,phone):
        for ph in self.phones:
            if ph.value == phone:
                self.phones.remove(ph)

    def edit_phone(self,old_phone,new_phone):
        Record.remove_phone(self,old_phone)
        Record.add_phone(self,new_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self,record):
           self.data[record.name.value] = record

    def find(self,name):
          for dict in self.data:
              if dict == name:
                  return self.data[name]
              else:
                  return None        
    def delete(self,name):
        del self.data[name] 
              
    def __str__(self):
        a=""
        for i in self.data:
            a = a + f"{self.data[i]}" + "\n"
        return a



