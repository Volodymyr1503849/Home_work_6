from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, name):
        self.name = name

class Phone(Field):
     def __init__(self, phone):
        if len(phone) == 10:
            self.phone = phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self,phone):
           self.phones.append(phone)
    def remove_phone(self,phone):
        if phone in self.phones:
            self.phones.remove(phone)
    def edit_phone(self,old_phone,new_phone):
        try:
            self.phones.remove(old_phone)
            self.phones.append(new_phone)  
        except ValueError:
              print("Введіть коректні дані")
    def find_phone(self,phone):
          for i in self.phones:
                if i == phone:
                      return phone
                else:
                      return None  
                    
class AddressBook(UserDict):
    def add_record(self,Record):
           self.data[Record.name.name] = Record.phones
           return self.data   
    def find(self,name):
          for i in self.data:
                if name == i :
                    return name
                else:
                    return  None
    def delete(self,name):
        try:
            del self.data[name]
            return self.data
        except:
              None           
    def __str__(self,Record):
        return f"Contact name: {Record.name.name}, phones: {'; '.join(p for p in Record.phones)}"
		
book = AddressBook()
phone_record = Phone("0663513021")
john_record = Record("John")
john_record.add_phone("0689688247")
john_record.add_phone("0689645457")
print(book.add_record(john_record))
print(john_record.edit_phone("0689645457","0984602460"))
found_phone = john_record.find_phone("0689688248")
print(book.__str__(john_record))
