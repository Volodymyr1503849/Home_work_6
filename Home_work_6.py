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
        if len(phone) != 10:
            raise Exception ("Введіть номер в десятковому форматі!")
        else:
            self.value = phone           

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
        try:
            for ph in self.phones:
                if ph.value == old_phone:
                    self.remove_phone(old_phone)
                    self.add_phone(new_phone)
                else:
                    return None
        except ValueError:
            print("Введіть коректні дані!") 
                 
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






