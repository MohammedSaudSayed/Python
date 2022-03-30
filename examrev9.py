contacts = {"Saud": "9930086525", "Danish": "8154936789"}

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
        
addContact("Aiman", "87543279870")
displayContact()

searchContact("Danish")
displayContact()

deleteContact("Danish")
displayContact()

updateContact("Saud", "8828567678")
displayContact()