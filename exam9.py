contacts = {"Saud": "9930086525", "Shahnawaz": "9786542312"}

def addContact(name, number):
    contacts[name] = number

def searchContact(name):
    if name in contacts:
        print(name, contacts[name])
    else:
        print("Contact not found")

def deleteContact(name):
    if name in contacts:
        del contacts[name]
    else:
        print(name, "not found")

def displayContact():
    for k,v in contacts.items():
        print(k,v)

def updateContact(name, number):
    if name in contacts:
        addContact(name, number)
    else:
        print("Contact not found")

addContact("Danish", "8765432179")
displayContact()

deleteContact("Danish")
displayContact()

searchContact("Ayan")
displayContact()

updateContact("Saud", 8338737738)
displayContact()