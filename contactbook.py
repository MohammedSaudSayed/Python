contact_book = {'Aiman': {'city': 'Mumbai',
                          'phone': '9892100046', 'email': 'aiman@gmail.com'},
                'Mariam': {'city': 'Sydney',
                           'phone': '9619591519', 'email': 'mariam@gmail.com'},
                'Sarah': {'city': 'Jeddah',
                          'phone': '8686864081', 'email': 'sarah@gmail.com'}}


def add_contact():
    name = input("Enter name: ")
    city = input("Enter city: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    if ((len(name) < 3) or (len(city) < 4) or (len(phone) < 10) or (len(email) < 8)):
        print("Error: Invalid fields")
        return

    contact_book[name] = {'city': city, 'phone': phone, 'email': email}


def search_contact(name):
    if name in contact_book:
        print("You searched " + name, contact_book[name])
    else:
        print("Contact not found")


def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
    else:
        print("Contact not found")


def update_contact(name):
    if name in contact_book:
        add_contact()
    else:
        print("Contact not found")


def print_contacts():
    print("\nContact list:")
    for k, v in contact_book.items():
        print(k, v['phone'])

# add_contact()

print(contact_book)
search_contact('Aiman')
# update_contact('Aiman')
delete_contact('Aiman')
print_contacts()