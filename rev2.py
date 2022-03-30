# Make a contact book which can add delete update display and search contacts of 5 people

contacts = {"Saud": "9930086525",
            "Nisar": "9167005160",
            "Almas": "9702166445",
            "Mehraan": "8167543216",
            "Kashaf": "3534262718"}

def addContact(name, number):
    contacts[name] = number

def searchContact(name):
    if name in contacts:
        print(name, contacts[name])
    else:
        print(name, "is not in your contacts")

def updateContact(name, number):
    if name in contacts:
        addContact(name, number)
    else:
        print("Contact not found")

def deleteContact(name):
    if name in contacts:
        del contacts[name]
    else:
        print("Contact not found")

def displayContact():
    for k,v in contacts.items():
        print(k,v)

addContact("Aman", "9870986754")
displayContact()

searchContact("Saud")
displayContact()

updateContact("Saud", 8765432219)
displayContact()

deleteContact("Kashaf")
displayContact()